import os
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"
import cv2
import re
import numpy as np
from paddleocr import PaddleOCR

# File picker
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_path = askopenfilename(title="Select ID Card Image")

if not file_path:
    print("No file selected ❌")
    exit()

# Load image
img = cv2.imread(file_path)

if img is None:
    print("Error loading image ❌")
    exit()

print("Image loaded ✅")

# Resize
img = cv2.resize(img, None, fx=2, fy=2)

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------- FACE EXTRACTION --------
import dlib

face_detector = dlib.get_frontal_face_detector()
faces = face_detector(gray)

if len(faces) == 0:
    print("No face detected ❌")

for face in faces:
    h, w = img.shape[:2]

    x1 = max(0, face.left())
    y1 = max(0, face.top())
    x2 = min(w, face.right())
    y2 = min(h, face.bottom())

    face_img = img[y1:y2, x1:x2]
    cv2.imwrite("id_face.jpg", face_img)
    print("Face extracted ✅")
    break
# --------------------------------

# -------- OCR SETUP (PaddleOCR) --------
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text_paddle(image):
    result = ocr.predict(image)

    extracted_text = []

    for res in result:
        if 'rec_texts' in res:
            extracted_text.extend(res['rec_texts'])

    return "\n".join(extracted_text)

# -------- IMAGE PREPROCESSING --------
gray = cv2.bilateralFilter(gray, 11, 17, 17)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Sharpen (VERY IMPORTANT for Paddle)
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
gray = cv2.filter2D(gray, -1, sharpen_kernel)

# Threshold
_, gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# -------- OCR --------
text_raw = extract_text_paddle(img)
text_proc = extract_text_paddle(gray)

text = text_raw + "\n" + text_proc
text = text.upper()

print("Raw OCR Text:\n", text)

# Keep formatting clean
text = re.sub(r'[ \t]+', ' ', text)

# -------------------------
# 🧠 DOCUMENT DETECTION
# -------------------------

doc_type = "UNKNOWN"

pan_pattern = re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text)
aadhaar_pattern = re.findall(r'\d{4}\s?\d{4}\s?\d{4}', text)

pan_keywords = [
    "INCOME", "TAX", "DEPARTMENT",
    "PERMANENT", "ACCOUNT", "NUMBER"
]

pan_keyword_score = sum(1 for word in pan_keywords if word in text)

if pan_pattern or pan_keyword_score >= 2:
    doc_type = "PAN"

elif aadhaar_pattern or ("AADHAAR" in text) or ("GOVERNMENT" in text and "INDIA" in text):
    doc_type = "AADHAAR"

print("Detected Document Type:", doc_type)

# Force PAN if pattern exists
if re.search(r'[A-Z]{5}[0-9]{4}[A-Z]', text):
    doc_type = "PAN"

# -------------------------
# 🔍 DATA EXTRACTION
# -------------------------

aadhaar = []
pan = "Not Found"
dob = []
gender = "Unknown"
name = ""
name_pan = ""
father_name = ""

# ---------- AADHAAR ----------
if doc_type == "AADHAAR":

    clean_text = re.sub(r'\b[6-9]\d{9}\b', '', text)
    matches = re.findall(r'\d{4}\s?\d{4}\s?\d{4}', clean_text)

    for m in matches:
        digits = re.sub(r'\D', '', m)
        if len(digits) == 12:
            aadhaar.append(digits)

    dob = re.findall(r'\d{2}[/\-]\d{2}[/\-]\d{4}', text)

    if "MALE" in text:
        gender = "Male"
    elif "FEMALE" in text:
        gender = "Female"

    # SMART NAME DETECTION
    lines = text.split("\n")
    candidates = []

    for line in lines:
        line = line.strip()

        clean_line = re.sub(r'[^A-Z ]', '', line)
        clean_line = re.sub(r'\s+', ' ', clean_line).strip()

        if len(clean_line) < 5:
            continue

        words = clean_line.split()

        if 2 <= len(words) <= 4:
            if any(word in ["MALE", "FEMALE", "GOVERNMENT", "INDIA", "AADHAAR", "MOBILE"] for word in words):
                continue

            score = len(clean_line)

            if all(word.isalpha() for word in words):
                score += 10

            if any(len(word) > 12 for word in words):
                score -= 10

            candidates.append((clean_line, score))

    if candidates:
        candidates = sorted(candidates, key=lambda x: x[1], reverse=True)
        name = candidates[0][0]

# ---------- PAN ----------
elif doc_type == "PAN":

    pan_matches = re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text)

    if pan_matches:
        pan = pan_matches[0]

    dob = re.findall(r'\d{2}[/\-]\d{2}[/\-]\d{4}', text)

    lines = text.split("\n")

    for line in lines:
        line_clean = line.strip()

        clean = re.sub(r'[^A-Z ]', '', line_clean)
        clean = re.sub(r'\s+', ' ', clean).strip()

        if len(clean) < 5:
            continue

        words = clean.split()

        if not (2 <= len(words) <= 4):
            continue

        if any(len(word) < 3 for word in words):
            continue

        if any(word in ["INCOME", "TAX", "DEPARTMENT", "GOVT", "INDIA", "ACCOUNT", "NUMBER"] for word in words):
            continue

        if name_pan == "":
            name_pan = clean
            continue

        if father_name == "":
            father_name = clean
            break

# -------------------------
# 📦 FINAL OUTPUT
# -------------------------

if doc_type == "AADHAAR":
    data = {
        "document": "Aadhaar",
        "name": name if name else "Not Found",
        "dob": dob[0] if dob else "Not Found",
        "aadhaar": aadhaar[0] if aadhaar else "Not Found",
        "gender": gender
    }

elif doc_type == "PAN":
    data = {
        "document": "PAN",
        "name": name_pan if name_pan else "Not Found",
        "father_name": father_name if father_name else "Not Found",
        "dob": dob[0] if dob else "Not Found",
        "pan": pan
    }

else:
    data = {
        "document": "Unknown",
        "message": "Could not detect document type"
    }

print("\n✅ Extracted Data:")
print(data)
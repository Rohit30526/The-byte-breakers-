import cv2
import pytesseract
import re


# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide tkinter window
Tk().withdraw()

# Open file dialog
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

# Resize (improves accuracy)
img = cv2.resize(img, None, fx=2, fy=2)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------- STEP 4: FACE EXTRACTION --------
import dlib

face_detector = dlib.get_frontal_face_detector()
faces = face_detector(gray)
if len(faces) == 0:
    print("No face detected ❌")
face_img = None

for i, face in enumerate(faces):
    h, w = img.shape[:2]

    x1 = max(0, face.left())
    y1 = max(0, face.top())
    x2 = min(w, face.right())
    y2 = min(h, face.bottom())

    face_img = img[y1:y2, x1:x2]
    cv2.imwrite("id_face.jpg", face_img)
    print("Face extracted ✅")
    break
# ----------------------------------------

# Improve contrast
gray = cv2.bilateralFilter(gray, 11, 17, 17)

# Sharpen image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Try OCR on BOTH images
text1 = pytesseract.image_to_string(gray, lang='eng')
text2 = pytesseract.image_to_string(gray, lang='hin')

text = text1 + "\n" + text2

# OCR
custom_config = r'--oem 3 --psm 6'

# OCR on original image
text_raw = pytesseract.image_to_string(img, config=custom_config, lang='eng+hin')

# OCR on processed (grayscale) image
text_proc = pytesseract.image_to_string(gray, config=custom_config, lang='eng+hin')

# Combine both texts
text = text_raw + "\n" + text_proc

print("Raw OCR Text:\n", text)

# -------------------------
# 🔍 DATA EXTRACTION
# -------------------------

# Aadhaar Number (XXXX XXXX XXXX)
aadhaar = re.findall(r'\d{4}\s?\d{4}\s?\d{4}', text)

# DOB
dob = re.findall(r'\d{2}[/\-]\d{2}[/\-]\d{4}', text)

# Gender
gender = "Unknown"
if "MALE" in text.upper():
    gender = "Male"
elif "FEMALE" in text.upper():
    gender = "Female"

# Name (best line detection)
lines = text.split("\n")
name = ""

for line in lines:
    line = line.strip()

    # Remove special characters
    clean_line = re.sub(r'[^A-Za-z ]', '', line)

    # Normalize spaces
    clean_line = re.sub(r'\s+', ' ', clean_line).strip()

    # ❌ Skip if empty
    if len(clean_line) == 0:
        continue

    # ❌ Skip lines without proper English words
    words = clean_line.split()

    # Must have 2–4 words
    if not (2 <= len(words) <= 4):
        continue

    # ❌ Reject short garbage words (like ae, be)
    if any(len(word) < 3 for word in words):
        continue

    # ❌ Skip unwanted keywords
    if any(word.upper() in ["MALE", "FEMALE", "GOVERNMENT", "INDIA", "AADHAAR", "MOBILE"] for word in words):
        continue

    # ✅ Valid name found
    name = clean_line
    break

# -------------------------
# 📦 FINAL OUTPUT
# -------------------------

data = {
    "name": name if name else "Not Found",
    "dob": dob[0] if dob else "Not Found",
    "aadhaar": aadhaar[0] if aadhaar else "Not Found",
    "gender": gender
}

print("\nExtracted Data:")
print(data)
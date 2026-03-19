import cv2
import pytesseract
import re

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
cap = cv2.VideoCapture(0)

print("Press 'c' to capture ID card")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture ID", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        img = frame.copy()
        cv2.imwrite("captured_id.jpg", img)
        print("Image captured ✅")
        break

    elif key == 27:  # ESC
        cap.release()
        cv2.destroyAllWindows()
        exit()

cap.release()
cv2.destroyAllWindows()

if img is None:
    print("Error: Image not found")
    exit()

# Resize (improves accuracy)
img = cv2.resize(img, None, fx=2, fy=2)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------- STEP 4: FACE EXTRACTION --------
import dlib

face_detector = dlib.get_frontal_face_detector()
faces = face_detector(gray)

face_img = None

for i, face in enumerate(faces):
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    face_img = img[y1:y2, x1:x2]
    cv2.imwrite("id_face.jpg", face_img)
    print("Face extracted ✅")
    break
# ----------------------------------------

# Apply threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# OCR
text = pytesseract.image_to_string(thresh, lang='eng+hin+mar')

print("Raw OCR Text:\n", text)

# -------------------------
# 🔍 DATA EXTRACTION
# -------------------------

# Aadhaar Number (XXXX XXXX XXXX)
aadhaar = re.findall(r'\d{4}\s\d{4}\s\d{4}', text)

# DOB
dob = re.findall(r'\d{2}/\d{2}/\d{4}', text)

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

    # Skip unwanted lines
    if any(word in line.upper() for word in ["MALE", "FEMALE", "GOVERNMENT", "INDIA", "AADHAAR"]):
        continue

    # Check for valid name (2–4 words, alphabet only)
    if re.match(r'^[A-Za-z]+\s[A-Za-z]+(\s[A-Za-z]+)?$', line):
        name = line
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
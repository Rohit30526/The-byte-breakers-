import cv2
import pytesseract
import re

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
img = cv2.imread("id_card2.jpeg")

if img is None:
    print("Error: Image not found")
    exit()

# Resize (improves accuracy)
img = cv2.resize(img, None, fx=2, fy=2)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
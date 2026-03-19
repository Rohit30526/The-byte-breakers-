import cv2
import pytesseract
import re

# ✅ Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocr_function(file_path):
    try:
        # 🔹 Load image
        img = cv2.imread(file_path)

        if img is None:
            return {"error": "Error loading image"}

        # 🔹 Resize (better accuracy)
        img = cv2.resize(img, None, fx=2, fy=2)

        # 🔹 Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 🔹 Improve image
        gray = cv2.bilateralFilter(gray, 11, 17, 17)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

        # 🔹 OCR config
        custom_config = r'--oem 3 --psm 6'

        # 🔹 Extract text
        text_raw = pytesseract.image_to_string(img, config=custom_config, lang='eng+hin')
        text_proc = pytesseract.image_to_string(gray, config=custom_config, lang='eng+hin')

        text = text_raw + "\n" + text_proc

        # -------------------------
        # 🔍 DATA EXTRACTION
        # -------------------------

        # Remove mobile numbers
        clean_text = re.sub(r'\b[6-9]\d{9}\b', '', text)

        # Aadhaar detection
        aadhaar = []
        matches = re.findall(r'\d{4}\s?\d{4}\s?\d{4}', clean_text)

        for m in matches:
            digits = re.sub(r'\D', '', m)
            if len(digits) == 12:
                aadhaar.append(digits)

        # DOB
        dob = re.findall(r'\d{2}[/\-]\d{2}[/\-]\d{4}', text)

        # Gender
        gender = "Not Found"
        if "MALE" in text.upper():
            gender = "Male"
        elif "FEMALE" in text.upper():
            gender = "Female"

        # Name detection
        lines = text.split("\n")
        name = ""

        for line in lines:
            line = line.strip()

            clean_line = re.sub(r'[^A-Za-z ]', '', line)
            clean_line = re.sub(r'\s+', ' ', clean_line).strip()

            if len(clean_line) == 0:
                continue

            words = clean_line.split()

            if not (2 <= len(words) <= 4):
                continue

            if any(len(word) < 3 for word in words):
                continue

            if any(word.upper() in ["MALE", "FEMALE", "GOVERNMENT", "INDIA", "AADHAAR", "MOBILE"] for word in words):
                continue

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

        return data

    except Exception as e:
        return {"error": str(e)}
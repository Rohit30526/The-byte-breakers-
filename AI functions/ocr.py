import cv2
import pytesseract
import re
import numpy as np

# ✅ Tesseract path (already installed in your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocr_function(file_path):
    try:
        # 🔹 Load image
        img = cv2.imread(file_path)
        if img is None:
            return {"error": "Error loading image"}

        # 🔹 Resize
        img = cv2.resize(img, None, fx=2, fy=2)

        # 🔹 Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 🔹 Improve image
        gray = cv2.bilateralFilter(gray, 11, 17, 17)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

        # 🔹 OCR
        custom_config = r'--oem 3 --psm 6'

        text_raw = pytesseract.image_to_string(img, config=custom_config, lang='eng')
        text_proc = pytesseract.image_to_string(gray, config=custom_config, lang='eng')

        text = (text_raw + "\n" + text_proc).upper()

        # -------------------------
        # 🔍 DATA EXTRACTION
        # -------------------------

        # Remove mobile numbers
        clean_text = re.sub(r'\b[6-9]\d{9}\b', '', text)

        # Aadhaar
        aadhaar = []
        matches = re.findall(r'\d{4}\s?\d{4}\s?\d{4}', clean_text)
        for m in matches:
            digits = re.sub(r'\D', '', m)
            if len(digits) == 12:
                aadhaar.append(digits)

        # PAN
        pan_pattern = re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text)
        pan = pan_pattern[0] if pan_pattern else "Not Found"

        # DOB
        dob = re.findall(r'\d{2}[/\-]\d{2}[/\-]\d{4}', text)

        # Gender
        gender = "Not Found"
        if "MALE" in text:
            gender = "Male"
        elif "FEMALE" in text:
            gender = "Female"

        # Name detection
        lines = text.split("\n")
        name = ""

        for line in lines:
            clean_line = re.sub(r'[^A-Z ]', '', line).strip()
            words = clean_line.split()

            if 2 <= len(words) <= 4:
                if any(word in ["MALE", "FEMALE", "GOVERNMENT", "INDIA", "AADHAAR"] for word in words):
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
            "pan": pan,
            "gender": gender
            
        }

        return data

    except Exception as e:
        return {"error": str(e)}
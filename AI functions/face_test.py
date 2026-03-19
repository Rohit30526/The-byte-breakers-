import face_recognition
import cv2
import numpy as np

# Load images
id_image = face_recognition.load_image_file("id_face.jpg")

# -------- STEP 4: SAFETY CHECK --------
if id_image is None:
    print("❌ ID face image not found (run OCR first)")
    exit()
# -------------------------------------
cap = cv2.VideoCapture(0)

print("Press 'c' to capture selfie")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Selfie", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        cv2.imwrite("selfie.jpg", frame)
        print("Selfie captured ✅")
        break

    elif key == 27:
        cap.release()
        cv2.destroyAllWindows()
        exit()

cap.release()
cv2.destroyAllWindows()

# Load captured selfie
selfie_image = face_recognition.load_image_file("selfie.jpg")

# Improve ID image
id_image = cv2.resize(id_image, None, fx=1.5, fy=1.5)

# Detect faces
id_locations = face_recognition.face_locations(id_image, model="hog")
selfie_locations = face_recognition.face_locations(selfie_image, model="hog")

if len(id_locations) == 0 or len(selfie_locations) == 0:
    print("❌ Face not detected")
    exit()

# Encode
id_encodings = face_recognition.face_encodings(id_image, id_locations)
selfie_encoding = face_recognition.face_encodings(selfie_image, selfie_locations)[0]

# Average encoding (better accuracy)
id_encoding = np.mean(id_encodings, axis=0)

# Compare
distance = face_recognition.face_distance([id_encoding], selfie_encoding)[0]

THRESHOLD = 0.48
match = distance < THRESHOLD

confidence = (1 - distance) * 100

print("\n Face Verification Result:")
print({
    "face_match": bool(match),
    "confidence": round(float(confidence), 2),
    "status": " Verified" if match else " Rejected"
})
import face_recognition
import cv2
import numpy as np

# Load images
id_image = face_recognition.load_image_file("id_card2.jpeg")
selfie_image = face_recognition.load_image_file("selfie.jpg")

# Improve ID image
id_image = cv2.resize(id_image, None, fx=1.5, fy=1.5)

# Detect faces
id_locations = face_recognition.face_locations(id_image, model="cnn")
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

print({
    "face_match": bool(match),
    "confidence": round(float(confidence), 2),
    "status": "Verified" if match else "Rejected"
})
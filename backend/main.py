from fastapi import FastAPI, UploadFile, File
from pymongo import MongoClient
from datetime import datetime
import sys
import os

# ✅ Create FastAPI app
app = FastAPI()

# ✅ MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["rakshakyc"]
collection = db["verifications"]

# ✅ Connect AI functions folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "AI functions")))

# ✅ Import OCR
from ocr import ocr_function


# ✅ Test route
@app.get("/")
def home():
    return {"message": "Backend running successfully"}


# ✅ MAIN API
@app.post("/verify")
async def verify(file: UploadFile = File(...)):

    # Validate file
    if not (file.content_type.startswith("image/") or file.content_type == "application/pdf"):
        return {"error": "Only image or PDF allowed"}

    # Read file
    contents = await file.read()

    # Save temp file
    temp_path = "temp.jpg"
    with open(temp_path, "wb") as f:
        f.write(contents)

    # 🔥 Run OCR
    try:
        ocr_result = ocr_function(temp_path)
    except Exception as e:
        return {"error": str(e)}

    # 🔥 Store in MongoDB
    data = {
        "document": {
            "filename": file.filename,
            "type": file.content_type
        },
        "ocr_data": ocr_result,
        "created_at": datetime.now()
    }

    collection.insert_one(data)

    # 🔥 Response
    return {
        "status": "success",
        "ocr_data": ocr_result
    }
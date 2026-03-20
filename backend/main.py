from fastapi import FastAPI, UploadFile, File
from pymongo import MongoClient
from datetime import datetime
import sys
import os
import uuid

# ✅ Create FastAPI app
app = FastAPI()

# ✅ MongoDB Atlas Connection
client = MongoClient("mongodb+srv://kadamsushant5328_db_user:Sitaram%40143@rakshakyc.kbnkrob.mongodb.net/rakshakyc?retryWrites=true&w=majority&appName=rakshakyc")
db = client["rakshakyc"]
collection = db["verifications"]

# ✅ Add AI functions folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "AI functions")))

# ✅ Import OCR function
from ocr import ocr_function


# ✅ Home route
@app.get("/")
def home():
    return {"message": "Backend running successfully"}


# ✅ Verify API (Upload → OCR → MongoDB)
@app.post("/verify")
async def verify(file: UploadFile = File(...)):

    try:
        # 🔹 Step 1: Validate file type
        if not (file.content_type.startswith("image/") or file.content_type == "application/pdf"):
            return {"error": "Only image or PDF allowed"}

        # 🔹 Step 2: Read file content
        contents = await file.read()

        # 🔹 Step 3: Create unique temp file
        temp_path = f"temp_{uuid.uuid4()}.jpg"

        with open(temp_path, "wb") as f:
            f.write(contents)

        # 🔹 Step 4: Run OCR
        ocr_result = ocr_function(temp_path)

        # 🔹 Step 5: Delete temp file (cleanup)
        os.remove(temp_path)

        # 🔹 Step 6: Prepare data for DB
        data = {
            "document": {
                "filename": file.filename,
                "type": file.content_type
            },
            "ocr_data": ocr_result,
            "verification_status": "pending",
            "created_at": datetime.now()
        }

        # 🔹 Step 7: Insert into MongoDB
        collection.insert_one(data)

        # 🔹 Step 8: Return response
        return {
            "status": "success",
            "message": "OCR processed & stored",
            "ocr_data": ocr_result
        }

    except Exception as e:
        return {"error": str(e)}
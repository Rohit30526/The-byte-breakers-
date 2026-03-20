import { useState } from "react";
import { useNavigate } from "react-router-dom";
import ProgressBar from "../components/kyc/ProgressBar";

export default function Upload() {
  const [doc, setDoc] = useState("");
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

  // 🔥 NEW: Handle Upload Function
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/verify" {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log("Response:", data);

      alert("OCR Done ✅");

      // 👉 Move to next step
      navigate("/selfie");

    } catch (error) {
      console.error("Error:", error);
      alert("Error connecting to backend ❌");
    }
  };

  return (
    <>
      {/* 🔥 Progress Bar */}
      <ProgressBar progress={25} />

      <div className="container">
        <div className="card">
          <h2>Upload Document</h2>

          {/* Select Document */}
          <select onChange={(e) => setDoc(e.target.value)}>
            <option value="">Choose Document</option>
            <option value="aadhaar">Aadhaar Card</option>
            <option value="pan">PAN Card</option>
          </select>

          {/* Upload File */}
          {doc && (
            <>
              <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
              />

              {file && (
                <p className="success">
                  ✔ Uploaded: {file.name}
                </p>
              )}

              {/* 🔥 FIXED BUTTON */}
              <button
                style={{ marginTop: "15px" }}
                onClick={handleUpload}
              >
                Continue →
              </button>
            </>
          )}
        </div>
      </div>
    </>
  );
}
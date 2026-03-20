import { useState } from "react";
import { useNavigate } from "react-router-dom";
import ProgressBar from "../components/kyc/ProgressBar";

export default function Upload() {
  const [doc, setDoc] = useState("");
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

  // 🔥 ONLY ADD THIS FUNCTION (no UI changes)
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/verify", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log("Response:", data);

      alert("OCR Done ✅");

      // ✅ KEEP YOUR FLOW SAME
      navigate("/selfie");

    } catch (error) {
      console.error("Error:", error);
      alert("Error connecting to backend ❌");
    }
  };

  return (
    <>
      {/* 🔥 Progress Bar (UNCHANGED) */}
      <ProgressBar progress={25} />

      <div className="container">
        <div className="card">
          <h2>Upload Document</h2>

          {/* Select Document (UNCHANGED) */}
          <select onChange={(e) => setDoc(e.target.value)}>
            <option value="">Choose Document</option>
            <option value="aadhaar">Aadhaar Card</option>
            <option value="pan">PAN Card</option>
          </select>

          {/* Upload File (UNCHANGED) */}
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

              {/* 🔥 ONLY CHANGE HERE */}
              <button
                style={{ marginTop: "15px" }}
                onClick={handleUpload}   // ✅ changed from navigate()
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
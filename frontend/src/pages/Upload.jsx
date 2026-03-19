import { useState } from "react";
import { useNavigate } from "react-router-dom";
import ProgressBar from "../components/kyc/ProgressBar";

export default function Upload() {
  const [doc, setDoc] = useState("");
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

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

              {/* Continue Button */}
              <button
                style={{ marginTop: "15px" }}
                onClick={() => navigate("/selfie")}
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
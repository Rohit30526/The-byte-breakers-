import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Upload() {
  const [doc, setDoc] = useState("");
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

  return (
    <div className="container">
      <div className="card">
        <h2>Upload Document</h2>

        <select onChange={(e) => setDoc(e.target.value)}>
          <option value="">Choose Document</option>
          <option value="aadhaar">Aadhaar Card</option>
          <option value="pan">PAN Card</option>
        </select>

        {doc && (
          <>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />

            {file && <p className="success">✔ Uploaded: {file.name}</p>}

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
  );
}
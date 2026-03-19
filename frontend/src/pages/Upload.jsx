import { useState } from "react";

export default function Upload() {
  const [doc, setDoc] = useState("");
  const [file, setFile] = useState(null);

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

            {file && (
              <p className="success">
                ✔ Uploaded: {file.name}
              </p>
            )}
          </>
        )}
      </div>
    </div>
  );
}
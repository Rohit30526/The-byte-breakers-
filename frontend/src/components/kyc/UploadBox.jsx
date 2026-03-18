import { useState } from "react";

function UploadBox() {

  // Stores uploaded file
  const [file, setFile] = useState(null);

  return (
    <div className="border-2 border-dashed p-6 text-center rounded-xl">

      <input
        type="file"

        // Save file when selected
        onChange={(e) => setFile(e.target.files[0])}
      />

      {/* Show file name after upload */}
      {file && (
        <p className="mt-4 text-green-600">
          {file.name}
        </p>
      )}

    </div>
  );
}

export default UploadBox;
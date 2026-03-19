"use client";

import { useState } from "react";

export default function UploadPage() {
  const [documentType, setDocumentType] = useState("");
  const [file, setFile] = useState<File | null>(null);

  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center">
      <div className="bg-zinc-900 p-6 rounded-2xl w-[350px] shadow-lg">
        <h1 className="text-xl font-bold mb-4">Upload Document</h1>

        {/* Dropdown */}
        <select
          value={documentType}
          onChange={(e) => setDocumentType(e.target.value)}
          className="w-full p-2 rounded bg-zinc-800 border border-zinc-700 mb-4"
        >
          <option value="">Select Document</option>
          <option value="aadhaar">Aadhaar Card *</option>
          <option value="pan">PAN Card *</option>
        </select>

        {/* Upload Section */}
        {documentType && (
          <div>
            <label className="text-sm text-gray-400">
              Upload {documentType === "aadhaar" ? "Aadhaar Card" : "PAN Card"}
            </label>

            <input
              type="file"
              onChange={(e) => setFile(e.target.files?.[0] || null)}
              className="mt-2 w-full p-2 bg-zinc-800 border border-zinc-700 rounded"
            />

            {/* Preview */}
            {file && (
              <p className="text-green-400 mt-2 text-sm">
                Uploaded: {file.name}
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
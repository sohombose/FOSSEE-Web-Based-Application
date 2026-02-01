import React, { useState } from "react";
import { uploadCSV } from "../services/api";

const FileUpload = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setMessage("");
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a CSV file");
      return;
    }

    try {
      await uploadCSV(file); // 🔥 if this doesn't throw → success

      setMessage("Upload successful ✅");
      setFile(null);

      if (onUploadSuccess) onUploadSuccess();
    } catch (error) {
      console.error(error);
      setMessage("Upload failed ❌");
    }
  };

  return (
    <div
      style={{
        backgroundColor: "#ffffff",
        padding: "20px",
        borderRadius: "12px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
        marginBottom: "30px",
      }}
    >
      <h3>Upload CSV</h3>

      <input type="file" accept=".csv" onChange={handleFileChange} />

      <br />
      <br />

      <button
        onClick={handleUpload}
        style={{
          padding: "10px 16px",
          backgroundColor: "#3498db",
          color: "white",
          border: "none",
          borderRadius: "6px",
          cursor: "pointer",
        }}
      >
        Upload
      </button>

      {message && (
        <p style={{ marginTop: "10px", fontWeight: "bold" }}>{message}</p>
      )}
    </div>
  );
};

export default FileUpload;

import React from "react";

export default function ScoreCard() {
  const data = [
    { step: "OCR", status: "Passed", score: 20 },
    { step: "Aadhaar", status: "Passed", score: 20 },
    { step: "PAN", status: "Failed", score: 0 },
    { step: "Liveness", status: "Passed", score: 20 },
    { step: "Face Match", status: "Failed", score: 0 },
  ];

  const totalScore = data.reduce((sum, item) => sum + item.score, 0);

  return (
    <div style={{
      height: "100vh",
      background: "#fafafa",
      padding: "20px"
    }}>

      {/* TITLE */}
      <h1 style={{
        textAlign: "center",
        marginBottom: "20px",
        fontSize: "28px",
        fontWeight: "600",
        color: "#333"
      }}>
        KYC Scorecard
      </h1>

      {/* TABLE */}
      <table style={{
        width: "100%",
        borderCollapse: "collapse",
        background: "#ffffff"
      }}>

        {/* HEADER */}
        <thead>
          <tr style={{ background: "#f1f5f9" }}>
            <th style={cell}>Step</th>
            <th style={cell}>Status</th>
            <th style={cell}>Score</th>
          </tr>
        </thead>

        {/* BODY */}
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td style={cell}>{item.step}</td>

              <td style={{
                ...cell,
                color: item.status === "Passed" ? "#16a34a" : "#dc2626"
              }}>
                {item.status}
              </td>

              <td style={cell}>{item.score}</td>
            </tr>
          ))}

          {/* TOTAL */}
          <tr style={{
            background: "#f8fafc",
            fontWeight: "600"
          }}>
            <td style={cell}>Total</td>
            <td style={cell}></td>
            <td style={cell}>{totalScore}</td>
          </tr>
        </tbody>

      </table>
    </div>
  );
}

const cell = {
  border: "1px solid #e5e7eb",
  padding: "14px",
  textAlign: "center",
  color: "#374151"
};
// Import React (needed to create components)
import React from "react";

// Create a function component (this is your page)
function Home() {
  
  // return = what UI will be shown on screen
  return (
    
    // Main container (full screen)
    <div style={styles.container}>
      
      {/* Card box in center */}
      <div style={styles.card}>
        
        {/* Title */}
        <h1 style={styles.title}>RakshaKYC AI 🚀</h1>
        
        {/* Subtitle */}
        <p style={styles.subtitle}>
          AI-powered identity verification system for secure and fast digital onboarding.
        </p>

        {/* Description */}
        <p style={styles.description}>
          Upload your documents, verify your identity, and complete KYC in seconds
          using advanced AI technologies like facial recognition, OCR, and fraud detection.
        </p>

        {/* Button */}
        <button 
          style={styles.button} 
          onClick={() => alert("Start KYC flow")}
        >
          Start KYC
        </button>

      </div>
    </div>
  );
}

// Export this component so other files can use it
export default Home;

// styles = JavaScript object for CSS
const styles = {
  
  // Full page styling
  container: {
    height: "100vh", // full screen height
    display: "flex", // flexbox layout
    justifyContent: "center", // center horizontally
    alignItems: "center", // center vertically
    background: "linear-gradient(135deg, #0f172a, #1e293b)",
    color: "#fff",
    fontFamily: "Arial, sans-serif",
  },

  // Card box styling
  card: {
    background: "#111827",
    padding: "40px",
    borderRadius: "16px",
    textAlign: "center",
    maxWidth: "500px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.5)",
  },

  // Title styling
  title: {
    fontSize: "32px",
    marginBottom: "10px",
  },

  // Subtitle styling
  subtitle: {
    fontSize: "16px",
    color: "#9ca3af",
    marginBottom: "20px",
  },

  // Description styling
  description: {
    fontSize: "14px",
    marginBottom: "30px",
    lineHeight: "1.5",
  },

  // Button styling
  button: {
    padding: "12px 24px",
    fontSize: "16px",
    borderRadius: "8px",
    border: "none",
    background: "#2563eb",
    color: "#fff",
    cursor: "pointer",
  },
};
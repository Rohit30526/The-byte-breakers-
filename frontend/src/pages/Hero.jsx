import { useNavigate } from "react-router-dom";

export default function Hero() {
  const navigate = useNavigate();

  return (
    <div className="container">
      <div className="card">
        <h1>Raksha KYC AI</h1>
        <p>Secure and fast identity verification</p>
        <button onClick={() => navigate("/upload")}>
          Start Verification →
        </button>
      </div>
    </div>
  );
}
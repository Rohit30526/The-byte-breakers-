import { useNavigate } from "react-router-dom";
import ProgressBar from "../components/kyc/ProgressBar";


export default function Hero() {
  const navigate = useNavigate();

  return (
    <>
      <ProgressBar progress={0} />

      <div className="container">
        <div className="card">
          <h1>Raksha KYC AI</h1>
          <p>Secure and fast identity verification powered by AI</p>

          <button onClick={() => navigate("/upload")}>
            Start Verification →
          </button>
        </div>
      </div>
    </>
  );
}
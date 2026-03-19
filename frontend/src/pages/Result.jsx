import { useNavigate } from "react-router-dom";
import ProgressBar from "../components/kyc/ProgressBar";


export default function Result() {
  const navigate = useNavigate();

  return (
    <>
      <ProgressBar progress={100} />

      <div className="container">
        <div className="card">
          <h2>Verification Complete</h2>
          <p className="success">✔ Your identity is verified</p>

          <button onClick={() => navigate("/")}>
            Back to Home
          </button>
        </div>
      </div>
    </>
  );
}
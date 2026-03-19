import { useNavigate } from "react-router-dom";

export default function Result() {
  const navigate = useNavigate();

  return (
    <div className="container">
      <div className="card">
        <h2>Verification Complete</h2>
        <p className="success">✔ Your identity is verified</p>

        <button onClick={() => navigate("/")}>
          Back to Home
        </button>
      </div>
    </div>
  );
}
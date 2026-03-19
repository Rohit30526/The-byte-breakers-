import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import ProgressBar from "../components/kyc/ProgressBar";


export default function Processing() {
  const navigate = useNavigate();

  useEffect(() => {
    setTimeout(() => {
      navigate("/result");
    }, 3000);
  }, []);

  return (
    <>
      <ProgressBar progress={75} />

      <div className="container">
        <div className="card">
          <h2>Processing...</h2>
          <p>Analyzing your data using AI</p>
        </div>
      </div>
    </>
  );
}
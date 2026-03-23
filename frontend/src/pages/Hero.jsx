import { useNavigate } from "react-router-dom";
import "../styles/hero.css";
import agentImg from "../assets/bot.jpg";
import { Shield, Globe, Zap } from "lucide-react";

export default function Hero() {
  const navigate = useNavigate();

  return (
    <>
      {/* HERO SECTION */}
      <section className="hero-container">

        {/* LEFT SIDE */}
        <div className="hero-left">
          <span className="badge">⚡ AI-POWERED KYC AGENT</span>

          <h1>
            Verify Identity <br />
            <span>Instantly.</span>
          </h1>

          <p>
            RakshaKYC AI automates customer onboarding with bank-grade security,
            facial recognition, and real-time fraud detection.
          </p>

          <div className="hero-buttons">
            <button
              onClick={() => navigate("/upload")}
              className="primary"
            >
              Start Verification
            </button>
          </div>

          {/* STATS */}
          <div className="hero-stats single">
            <div className="stat">
              <h3>99.9%</h3>
              <p>Accuracy</p>
            </div>
          </div>
        </div>
        {/* RIGHT SIDE CARD */}
        <div className="hero-right">
          <div className="ai-card">
            <img src={agentImg} alt="AI Agent" className="agent-img" />

            <h3>Raksha AI Agent</h3>

            <p>
              "I'm ready to verify your identity. Please have your government ID ready."
            </p>

            <div className="progress-bar">
              <div className="progress"></div>
            </div>

            <span className="status">SYSTEM READY</span>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section className="features">
        <div className="feature">
          <div className="feature-icon">
            <Shield size={20} />
          </div>

          <h4>Bank-Grade Security</h4>
          <p>
            End-to-end encrypted verification process compliant with global standards.
          </p>
        </div>

        <div className="feature">
          <div className="feature-icon">
            <Globe size={20} />
          </div>

          <h4>Multilingual Support</h4>
          <p>
            AI voice assistance in 50+ languages to guide users through every step.
          </p>
        </div>

        <div className="feature">
          <div className="feature-icon">
            <Zap size={20} />
          </div>
          <h4>Instant Results</h4>
          <p>
            OCR and biometric matching completed in seconds, not minutes.
          </p>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="footer">
        <div className="footer-left">🛡️ RakshaKYC AI</div>

        <div className="footer-center">
          <span>Privacy Policy</span>
          <span>Terms of Service</span>
          <span>Compliance</span>
        </div>

        <div className="footer-right">
          © 2026 RakshaKYC AI. All rights reserved.
        </div>
      </footer>
    </>
  );
}
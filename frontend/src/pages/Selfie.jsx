import { useRef, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Selfie() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const [cameraOn, setCameraOn] = useState(false);
  const [image, setImage] = useState(null);

  const navigate = useNavigate();

  // 🔥 Start camera (only change state)
  const startCamera = () => {
    setCameraOn(true);
  };

  // 🔥 Attach stream AFTER video renders
  useEffect(() => {
    if (cameraOn && videoRef.current) {
      navigator.mediaDevices
        .getUserMedia({ video: true })
        .then((stream) => {
          videoRef.current.srcObject = stream;
          videoRef.current.play();
        })
        .catch((err) => {
          console.error("Camera error:", err);
          alert("Camera not working");
        });
    }
  }, [cameraOn]);

  // Capture photo
  const capturePhoto = () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    const imageData = canvas.toDataURL("image/png");
    setImage(imageData);
  };

  // Retry
  const retryPhoto = () => {
    setImage(null);
  };

  return (
    <div className="container">
      <div className="card">
        <h2>Capture Selfie</h2>

        {/* STEP 1 */}
        {!cameraOn && !image && (
          <button onClick={startCamera}>
            Open Camera 📷
          </button>
        )}

        {/* STEP 2 */}
        {cameraOn && !image && (
          <>
            <video
              ref={videoRef}
              autoPlay
              playsInline
              muted
              style={{ width: "100%", borderRadius: "10px" }}
            />

            <button onClick={capturePhoto} style={{ marginTop: "10px" }}>
              Capture Photo
            </button>
          </>
        )}

        {/* STEP 3 */}
        {image && (
          <>
            <img
              src={image}
              alt="Captured"
              style={{ width: "100%", borderRadius: "10px" }}
            />

            <div style={{ marginTop: "10px" }}>
              <button onClick={retryPhoto} style={{ marginRight: "10px" }}>
                Retry 🔄
              </button>

              <button onClick={() => navigate("/processing")}>
                Continue →
              </button>
            </div>
          </>
        )}

        <canvas ref={canvasRef} style={{ display: "none" }}></canvas>
      </div>
    </div>
  );
}
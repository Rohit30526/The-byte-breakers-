
import React, { useRef, useEffect, useState } from "react";

function CameraFrame({ onCapture }) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [stream, setStream] = useState(null);

  // Start camera
  useEffect(() => {
    const startCamera = async () => {
      try {
        const mediaStream = await navigator.mediaDevices.getUserMedia({
          video: true,
        });
        videoRef.current.srcObject = mediaStream;
        setStream(mediaStream);
      } catch (err) {
        console.error("Error accessing camera:", err);
      }
    };

    startCamera();

    return () => {
      // Stop camera on unmount
      if (stream) {
        stream.getTracks().forEach((track) => track.stop());
      }
    };
  }, []);

  // Capture image
  const handleCapture = () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    const imageData = canvas.toDataURL("image/png");

    if (onCapture) {
      onCapture(imageData);
    }
  };

  return (
    <div className="camera-container">
      {/* Camera Feed */}
      <video
        ref={videoRef}
        autoPlay
        playsInline
        className="camera-video"
      />

      {/* Overlay Frame */}
      <div className="camera-overlay">
        <div className="frame"></div>
      </div>

      {/* Capture Button */}
      <button className="capture-btn" onClick={handleCapture}>
        Capture
      </button>

      {/* Hidden canvas */}
      <canvas ref={canvasRef} style={{ display: "none" }} />
    </div>
  );
}

export default CameraFrame;


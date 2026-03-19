export default function ProgressBar({ progress }) {
  return (
    <div style={{ width: "100%", background: "#eee", height: "6px" }}>
      <div
       style={{
    width: `${progress}%`,
    height: "100%",
    background: "linear-gradient(90deg, gold, orange)",
    transition: "width 0.6s ease-in-out",
  }}
      />
    </div>
  );
}
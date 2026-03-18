import { useNavigate } from "react-router-dom";

// Import UI components
import Button from "../components/ui/Button";
import Container from "../components/layout/Container";
import Navbar from "../components/layout/Navbar";

function Home() {

  // Used to move between pages
  const navigate = useNavigate();

  return (
    <>
      <Navbar />

      <Container>

        <div className="flex flex-col items-center justify-center h-[80vh] text-center">

          <h1 className="text-4xl font-bold mb-4">
            AI-Powered KYC Verification
          </h1>

          <p className="mb-6 text-gray-600">
            Fast, Secure and Automated Identity Verification
          </p>

          {/* Navigate to upload page */}
          <Button
            text="Start KYC"
            onClick={() => navigate("/upload")}
          />

        </div>

      </Container>
    </>
  );
}

export default Home;
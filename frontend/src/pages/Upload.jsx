import UploadBox from "../components/kyc/UploadBox";

import Navbar from "../components/layout/Navbar";
import Container from "../components/layout/Container";

function Upload() {

  return (
    <>
      <Navbar />

      <Container>

        <h2 className="text-2xl font-semibold mb-4">
          Upload Your Document
        </h2>

        <UploadBox />

      </Container>
    </>
  );
}

export default Upload;
// Import routing tools
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Import your pages (based on your structure)
import Home from "../pages/Home";
import Upload from "../pages/Upload";
import Selfie from "../pages/Selfie";
import Result from "../pages/Result";

// ⚠️ IMPORTANT: If Processing.jsx not created yet, comment it for now
// import Processing from "../pages/Processing";

function AppRoutes() {
  return (
    // Enables routing in entire app
    <BrowserRouter>

      {/* Defines all routes */}
      <Routes>

        {/* Home page */}
        <Route path="/" element={<Home />} />

        {/* Upload page */}
        <Route path="/upload" element={<Upload />} />

        {/* Selfie page */}
        <Route path="/selfie" element={<Selfie />} />

        {/* Add later when created */}
        {/* <Route path="/processing" element={<Processing />} /> */}

        {/* Result page */}
        <Route path="/result" element={<Result />} />

      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;
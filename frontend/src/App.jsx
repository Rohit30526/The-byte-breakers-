import { BrowserRouter, Routes, Route } from "react-router-dom";

import Hero from "./pages/Hero";
import Upload from "./pages/Upload";
import Selfie from "./pages/Selfie";
import Processing from "./pages/Processing";
import Result from "./pages/Result";
import ScoreCard from "./components/kyc/Scorecard.jsx";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Hero />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/selfie" element={<Selfie />} />
        <Route path="/processing" element={<Processing />} />
        <Route path="/result" element={<Result />} />
        <Route path="/scorecard" element={<ScoreCard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
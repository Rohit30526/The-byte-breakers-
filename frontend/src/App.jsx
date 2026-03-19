import { BrowserRouter, Routes, Route } from "react-router-dom";

import Hero from "./pages/Hero";
import Upload from "./pages/Upload";
import Selfie from "./pages/Selfie";
import Processing from "./pages/Processing";
import Result from "./pages/Result";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Hero />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/selfie" element={<Selfie />} />
        <Route path="/processing" element={<Processing />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
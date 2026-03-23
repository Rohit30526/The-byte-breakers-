import { BrowserRouter, Routes, Route } from "react-router-dom";
import Hero from "../pages/Hero";
import Upload from "../pages/Upload";
import Selfie from "../pages/Selfie";
import Processing from "../pages/Processing";
import Result from "../pages/Result";
import MainLayout from "../Layouts/MainLayout";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Hero />} />
          <Route path="/upload" element={<Upload />} />
          <Route path="/selfie" element={<Selfie />} />
          <Route path="/processing" element={<Processing />} />
          <Route path="/result" element={<Result />} />
        </Routes>
      </MainLayout>
    </BrowserRouter>
  );
}
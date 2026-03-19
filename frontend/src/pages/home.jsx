export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-100 to-purple-100">

      <div className="text-center">
        
        {/* Title */}
        <h1 className="text-4xl font-bold text-gray-800 mb-3">
          Raksha KYC AI
        </h1>

        {/* Subtitle */}
        <p className="text-gray-500 mb-8">
          Secure and Fast Identity Verification
        </p>

        {/* Button */}
        <button className="px-6 py-3 rounded-lg text-white font-medium 
          bg-gradient-to-r from-blue-500 to-purple-600 
          hover:scale-105 transition shadow-lg">
          Start KYC →
        </button>

      </div>

    </div>
  );
}
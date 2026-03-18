function Button({ text, onClick }) {

  return (
    <button
      onClick={onClick} // triggers action

      className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-xl transition"
    >
      {text}
    </button>
  );
}

export default Button;
import React, { useState, useEffect } from "react";
import "./App.css";
import { getWhiteCards } from "./services/graphQl";

function App() {
  const [whiteCards, setWhiteCards] = useState([]);

  async function getWhites() {
    const whiteCards = await getWhiteCards();
    setWhiteCards(whiteCards);
  }

  useEffect(() => {
    getWhites();
  }, []);

  return (
    <div className="App">
      <div cards={whiteCards} />
    </div>
  );
}

export default App;

import React, { useState, useEffect } from "react";
import "./App.css";
import { getWhiteCards, getBlackCards } from "./services/graphQl";

function App() {
  const [whiteCards, setWhiteCards] = useState([]);
  const [blackCards, setBlackCards] = useState([]);

  async function getCards() {
    const whiteCards = await getWhiteCards();
    const blackCards = await getBlackCards();
    setWhiteCards(whiteCards);
    setBlackCards(blackCards);
  }

  useEffect(() => {
    getCards();
  }, []);

  return (
    <div className="App">
      <div
        whiteCards={whiteCards}
        blackCards={blackCards}
      />
    </div>
  );
}

export default App;

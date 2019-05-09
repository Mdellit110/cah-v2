import React, { useState, useEffect } from "react";
import "./App.css";
import { getCards } from "./services/graphQl";
import Deck from "./components/Deck";

function App() {
  const [whiteCards, setWhiteCards] = useState([]);
  const [blackCards, setBlackCards] = useState([]);

  async function getDecks() {
    const cards = await getCards(`["90s", "CAHe3"]`);
    console.log(cards);
    setWhiteCards(cards.whiteDecks);
    setBlackCards(cards.blackDecks);
  }

  useEffect(() => {
    getDecks();
  }, []);

  return (
    <div className="App">
      <Deck color="black" cards={blackCards} />
      <Deck color="white" cards={whiteCards} />
    </div>
  );
}

export default App;

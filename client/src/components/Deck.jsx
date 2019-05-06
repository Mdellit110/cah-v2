import React from "react";
const Deck = props => {
  const { cards, color } = props;
  return (
    <div className={`${color} deck`}>
      {cards.map(card => (
        <p>
          {`${color}:
          ${card.text}`}
        </p>
      ))}
    </div>
  );
};
export default Deck;

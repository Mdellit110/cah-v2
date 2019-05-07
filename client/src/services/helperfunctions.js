function filterDecks() {
  let lastCard;
  const filtered = blackCards
    .filter((card, i, blackCards) => {
      if (i === 0) return true;
      let lastCard = blackCards[i - 1];
      return card.deck !== lastCard.deck;
    })
    .map(card => card.deck);
  console.log(filtered);
}

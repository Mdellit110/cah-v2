import axios from "axios";

// TODO: set the Search field to a param

const getCards = async decks => {
  const resp = await axios({
    url: "http://127.0.0.1:8000",
    method: "post",
    data: {
      query: `{
        whiteDecks(deck: ${decks}) {
          deck
          text
        }
        blackDecks(deck: ${decks}) {
          deck
          text
          pick
        }
      }`
    }
  });
  return resp.data.data;
};

export { getCards };

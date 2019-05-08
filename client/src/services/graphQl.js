import axios from "axios";

// TODO: set the Search field to a param

const getCards = async args => {
  const resp = await axios({
    url: "http://127.0.0.1:8000",
    method: "post",
    data: {
      query: `{
        first: decks(deck: "90s") {
          __typename
          ... on WhiteCard{
            text,
            deck
          }
          ... on BlackCard{
            text,
            deck,
            pick
          }
        }
        second: decks(deck: "apples") {
          __typename
          ... on WhiteCard{
            text,
            deck
          }
          ... on BlackCard{
            text,
            deck,
            pick
          }
        }
      }`
    }
  });
  return resp.data.data;
};

export { getCards };

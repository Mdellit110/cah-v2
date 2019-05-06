import axios from "axios";

// TODO: set the Search field to a param

const getCards = async () => {
  const resp = await axios({
    url: "http://127.0.0.1:8000",
    method: "post",
    data: {
      query: `{
        search(deck: "90s") {
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
  console.table(resp.data.data.search);
  return resp.data.data.search;
};

export { getCards };

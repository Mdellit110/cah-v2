import axios from "axios";

const getWhiteCards = async () => {
  const resp = await axios({
    url: "http://127.0.0.1:8000",
    method: "post",
    data: {
      query: `{ allWhitecards { edges { node { id deck text } } } }`
    }
  });

  return resp.data.data.allWhitecards;
};

const getBlackCards = async () => {
  const resp = await axios({
    url: "http://127.0.0.1:8000",
    method: "post",
    data: {
      query: `{ allBlackcards { edges { node { id deck text } } } }`
    }
  });

  return resp.data.data.allBlackcards;
};

export {
  getWhiteCards,
  getBlackCards
 };

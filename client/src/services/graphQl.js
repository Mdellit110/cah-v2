import axios from "axios";

const getWhiteCards = async () => {
  const resp = await axios({
    url: "http://127.0.0.1:8000",
    method: "post",
    data: {
      query: `{ allWhitecards { edges { node { id deck text } } } }`
    }
  });
  console.log(resp.data.data.allWhitecards.edges);

  return resp.data.data.allWhitecards;
};

export { getWhiteCards };

import React, { useState} from "react";
import "./App.css";
import { getWhiteCards } from './services/graphQl'

function App() {
  getWhiteCards()
  return (
    <div className="App" >
    </div>
  )
}

export default App;

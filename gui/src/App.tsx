import { useState } from "react";
import "./App.css";
import Chat from "./components/Chat";
import NavMenu from "./components/NavMenu";

function App() {
  const [showHome, setShowHome] = useState(true);

  return (
    <div className="flex-col">
      <NavMenu setShowHome={setShowHome}/>
      <Chat setShowHome={setShowHome} showHome={showHome}/>
    </div>
  );
}

export default App;

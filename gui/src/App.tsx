import { useState } from "react";
import "./App.css";
import Chat from "./components/Chat";
import NavMenu from "./components/NavMenu";
import useSpeechSynthesis from "./components/useSpeachSyntesis";


function App() {
  const [showHome, setShowHome] = useState(true);
  const { speaking, speak, cancel, voices, selectedVoice, setSelectedVoice } = useSpeechSynthesis();

  return (
    <div className="flex-col">
      <NavMenu setShowHome={setShowHome} voices={voices} selectedVoice={selectedVoice} setSelectedVoice={setSelectedVoice}/>
      <Chat setShowHome={setShowHome} showHome={showHome} speaking={speaking} speak={speak} cancel={cancel}/>
    </div>
  );
}

export default App;

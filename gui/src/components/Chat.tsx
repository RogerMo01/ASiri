import ChatInput from "./ChatInput";
import ChatHistory from "./ChatHistory";
import "./Chat.css"
import { useEffect, useState } from "react";

const defaultResponse = "Hey there, I can help you with anything you want, you just give me a touch when yo need something from me, I am you assistant in every moment";

function Chat() {
  const [lastUserMessage, setLastUserMessage] = useState("");
  const [lastResponse, setLastResponse] = useState("");

  useEffect(() => {
    if (lastUserMessage !== ""){
      alert(`Cambio el msg: ${lastUserMessage}`)

      // Pedir respuesta del asistente
      setLastResponse(defaultResponse)

    }
  }, [lastUserMessage]);

  return (
    <div className="full-box mx-auto p-4 max-w-7xl">
      <ChatHistory userMsg={lastUserMessage} assistantMsg={lastResponse}/>
      <ChatInput setter={setLastUserMessage}/>
    </div>
  );
}

export default Chat;

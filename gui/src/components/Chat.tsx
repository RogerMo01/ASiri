import ChatInput from "./ChatInput";
import ChatHistory from "./ChatHistory";
import { useEffect, useState } from "react";

const defaultResponse = "Hey there, I can help you with anything you want, you just give me a touch when yo need something from me, I am you assistant in every moment. Hey there, I can help you with anything you want, you just give me a touch when yo need something from me, I am you assistant in every moment";

function Chat() {
  const [lastUserMessage, setLastUserMessage] = useState("");
  const [lastResponse, setLastResponse] = useState("");

  useEffect(() => {
    if (lastUserMessage !== ""){

      // Pedir respuesta del asistente
      setLastResponse(defaultResponse);

    }
    else{
      setLastResponse("");
    }
  }, [lastUserMessage]);

  return (
    <div className="flex-col p-4 lg:mx-40 rounded-xl">
      <ChatHistory userMsg={lastUserMessage} assistantMsg={lastResponse}/>
      <ChatInput setter={setLastUserMessage}/>
    </div>
  );
}

export default Chat;

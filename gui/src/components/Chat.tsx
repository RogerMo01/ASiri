import ChatInput from "./ChatInput";
import ChatHistory from "./ChatHistory";
import { useEffect, useState } from "react";

const defaultResponse = "Hey there, I can help you with anything you want, you just give me a touch when you need something from me, I am your assistant in every moment.";

function Chat() {
  const [lastUserMessage, setLastUserMessage] = useState("");
  const [lastResponse, setLastResponse] = useState("");

  useEffect(() => {
    const fetchResponse = async () => {
      if (lastUserMessage !== "") {

        // Temporal displayed response
        setLastResponse("");

        // (DELETE) Simulate wait
        await new Promise(resolve => setTimeout(resolve, 3000));
        
        // Request assistant response
        setLastResponse(defaultResponse);

      } else {
        setLastResponse("");
      }
    };

    fetchResponse();
  }, [lastUserMessage]);

  return (
    <div className="flex-col p-4 lg:mx-40 rounded-xl">
      <ChatHistory userMsg={lastUserMessage} assistantMsg={lastResponse}/>
      <ChatInput setter={setLastUserMessage}/>
    </div>
  );
}

export default Chat;

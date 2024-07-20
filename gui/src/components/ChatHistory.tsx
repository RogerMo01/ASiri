import ChatAssistantMsg from "./ChatAssistantMsg";
import ChatUserMsg from "./ChatUserMsg";

interface Props {
  userMsg: string;
  assistantMsg: string;
}


function ChatHistory({ userMsg, assistantMsg }: Props) {
  const active = userMsg !== "" || assistantMsg !== "";
  return (
    <div className="flex-grow">
      {active && <div>
        <ChatUserMsg msg={userMsg}/>
        <ChatAssistantMsg msg={assistantMsg}/>
      </div>}
      {!active && <div>
        {/* <img src="/brand.png" className="max-h-60"/> */}
      </div>}

    </div>
  );
}

export default ChatHistory;

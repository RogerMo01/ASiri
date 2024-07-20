import ChatAssistantMsg from "./ChatAssistantMsg";
import ChatUserMsg from "./ChatUserMsg";

interface Props {
  userMsg: string;
  assistantMsg: string;
}


function ChatHistory({ userMsg, assistantMsg }: Props) {
  const active = userMsg !== "" || assistantMsg !== "";
  return (
    <div className="flex-grow flex-col h-auto justify-center">
      {active && <div>
        <ChatUserMsg msg={userMsg}/>
        <ChatAssistantMsg msg={assistantMsg}/>
      </div>}
      {!active && <>
        <div className="text-3xl text-gray-400 flex-col h-auto items-center">
          <img src="/logo_cold.gif" className="w-28 mb-4"/>
          Ask something to ASiri
        </div>
      </>}
    </div>
  );
}

export default ChatHistory;

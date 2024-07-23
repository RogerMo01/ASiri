import ChatAssistantMsg from "./ChatAssistantMsg";
import ChatUserMsg from "./ChatUserMsg";

interface Props {
  userMsg: string;
  assistantMsg: string;
  thinking: boolean;
  showHome: boolean;
  lastWasAudio: boolean;
}


function ChatHistory({ userMsg, assistantMsg, thinking, showHome, lastWasAudio }: Props) {
  return (
    <div className="flex-grow flex-col h-auto justify-center">

      {!showHome && <div>
        {!lastWasAudio && <ChatUserMsg msg={userMsg}/>}
        <ChatAssistantMsg msg={assistantMsg} thinking={thinking}/>
      </div>}

      {showHome && <>
        <div className="text-3xl text-gray-400 flex-col h-auto items-center">
          <img src="/logo_cold.gif" className="w-28 mb-4"/>
          Ask something to ASiri
        </div>
      </>}

    </div>
  );
}

export default ChatHistory;

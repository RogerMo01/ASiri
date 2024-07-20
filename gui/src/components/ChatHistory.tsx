import "./ChatHistory.css"

interface Props{
    userMsg: string,
    assistantMsg: string
}

function ChatHistory({userMsg, assistantMsg}: Props) {

  return (
    <div className="history-div min-h-10vh">
        <h1>History</h1>
        <p>{userMsg}</p>
        <p>{assistantMsg}</p>
    </div>
  );
}

export default ChatHistory;

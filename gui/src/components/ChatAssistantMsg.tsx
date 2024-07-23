import { useEffect, useState } from "react";

interface Props {
  msg: string;
  thinking: boolean;
}

function ChatAssistantMsg({ msg, thinking }: Props) {
  const [displayedMessage, setDisplayedMessage] = useState("");
  const words: string[] = msg.split(" ");

  useEffect(() => {
    if (words.length === 0) return;

    let index = 0;
    const intervalId = setInterval(() => {
      setDisplayedMessage(() => {
        const newMessage = words.slice(0, index + 1).join(" ");
        return newMessage;
      });
      index++;
      if (index >= words.length) {
        clearInterval(intervalId);
      }
    }, 50);

    return () => clearInterval(intervalId);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [msg]);

  return (
    <div className="flex m-2 my-6">
      {!thinking && <div className="max-w-12 min-w-12">
        <img src="/logo.png" alt="Logo"/>
      </div>}
      {thinking && <div className="max-w-12 min-w-12">
        <img src="/logo_animated.gif" alt="Animated Logo"/>
      </div>}
      <div className="bg-gray-200 flex-grow border border-gray-300 mx-2 rounded-2xl p-2 text-left">
        {thinking ? "" : displayedMessage}
      </div>
    </div>
  );
}

export default ChatAssistantMsg;
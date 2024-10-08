import { SetStateAction, useRef, useState } from "react";
import { IoMdSend } from "react-icons/io";
import RecordButton from "./RecordButton";

interface Props{
  setter: React.Dispatch<SetStateAction<string>>,
  audioURLSetter: React.Dispatch<SetStateAction<string>>,
  loading: boolean
}

function ChatInput({setter, audioURLSetter, loading}: Props) {
  const textArea = useRef<HTMLTextAreaElement>(null);
  const [message, setMessage] = useState("");

  const handleChange = (event: {
    target: { value: SetStateAction<string> };
  }) => {
    setMessage(event.target.value);

    if (textArea.current) {
      textArea.current.style.height = "auto";
      textArea.current.style.height = `${textArea.current.scrollHeight}px`;
    }
  };

  const handleSend = () => {
    console.log(`[*] User has sent: ${message}`)
    setter(message);
    setMessage("");
    if (textArea.current) {
      textArea.current.style.height = "auto";
    }
  };

  const handleKeyPress = (event: { key: string; shiftKey: unknown; preventDefault: () => void; }) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      handleSend();
    }
  };
  

  return (
    <div className="mt-4 p-1 flex bg-gray-200 border border-gray-500 rounded-xl">
      <textarea
        ref={textArea}
        value={message}
        disabled={loading}
        onChange={handleChange}
        onKeyDown={handleKeyPress}
        className="input-box resize-none mr-2 w-full rounded-xl bg-gray-200 font-normal text-base pr-4 py-2 pl-4 overflow-hidden"
      ></textarea>
      <div className="flex items-end">
        <RecordButton style="h-16 w-auto mx-1 pr-2 pl-2" audioURLSetter={audioURLSetter} loading={loading} />
        <button onClick={() => handleSend()} className="h-16 w-auto rounded-full pr-2 pl-2" disabled={loading}>
          <IoMdSend size={25}/>
        </button>
      </div>
    </div>
  );
}

export default ChatInput;

import { SetStateAction, useRef, useState } from "react";
import { IoMdSend } from "react-icons/io";
import "./ChatInput.css";

interface Props{
    setter: React.Dispatch<SetStateAction<string>>
}

function ChatInput({setter}: Props) {
  const textArea = useRef<HTMLTextAreaElement>(null);
  const [message, setMessage] = useState("");

  const handleChange = (event: {
    target: { value: SetStateAction<string> };
  }) => {
    setMessage(event.target.value);
    console.log(event.target.value);

    if (textArea.current) {
      textArea.current.style.height = "auto";
      textArea.current.style.height = `${textArea.current.scrollHeight}px`;
    }
  };

  const handleSend = () => {
    console.log(`[*] User has sent: ${message}`)
    setter(message);
    setMessage("");
  };

  return (
    <div className="mt-4 p-1 flex">
      <textarea
        ref={textArea}
        value={message}
        onChange={handleChange}
        className="input-box resize-none h-auto mr-2 w-full rounded-xl bg-gray-100 font-normal text-base pr-4 py-2 pl-4 overflow-hidden"
      ></textarea>
      <button onClick={() => handleSend()} className="h-12 pr-2 pl-2">
        <IoMdSend size={30}/>
      </button>
    </div>
  );
}

export default ChatInput;

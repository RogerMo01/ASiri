import { useEffect, useState } from "react";
import useSpeechSynthesis from "./useSpeachSyntesis";
import { RiSpeakFill } from "react-icons/ri";
import { HiSpeakerWave } from "react-icons/hi2";
import { FaStopCircle } from "react-icons/fa";

interface Props {
  msg: string;
  thinking: boolean;
  lastWasAudio: boolean;
}

function ChatAssistantMsg({ msg, thinking, lastWasAudio }: Props) {
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


  // Speech to Text hook
  const { speaking, speak, cancel } = useSpeechSynthesis();
  

  // Read aloud when response changes
  useEffect(() => {
    if (msg && lastWasAudio) {
      speak(msg);
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [msg])
  


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
        {!thinking && <div className="flex justify-end mr-2">
          {!speaking && <HiSpeakerWave className="cursor-pointer" size={20} color="gray" onClick={() => speak(msg)}/>}
          {speaking && <FaStopCircle className="cursor-pointer" size={20} color="gray" onClick={cancel}/>}
        </div>}
      </div>
      
    </div>
  );
}

export default ChatAssistantMsg;
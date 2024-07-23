import { SetStateAction, useRef, useState } from "react";
import { FaMicrophone } from "react-icons/fa";
import { FaStopCircle } from "react-icons/fa";
import Timer from "./Timer";
import "./RecordButton.css"

interface Props {
  style: string;
  audioURLSetter: React.Dispatch<SetStateAction<string>>;
  loading: boolean;
}

function RecordButton({ style, audioURLSetter, loading }: Props) {
  const [isRecording, setIsRecording] = useState(false);
  const mediaRecorder = useRef<MediaRecorder | null>(null);
  const audioChunks = useRef<Blob[]>([]);

  const startRecording = async () => {
    try{
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder.current = new MediaRecorder(stream);
    
        mediaRecorder.current.ondataavailable = (event) => {
          audioChunks.current.push(event.data);
        };
    
        mediaRecorder.current.onstop = () => {
          const blob = new Blob(audioChunks.current, { type: "audio/wav" });
          const url = URL.createObjectURL(blob);
          audioURLSetter(url);
          audioChunks.current = [];
        };
    
        mediaRecorder.current.start();
        setIsRecording(true);
    } catch(error){
        console.error('Error accessing the microphone:', error);
        alert('🎙 Cannot access to microphone because we are not using HTTPS protocol!');
    }
  };

  const stopRecording = () => {
    mediaRecorder.current?.stop();
    setIsRecording(false);
  };

  return (
    <>
      <button
        onClick={isRecording ? stopRecording : startRecording}
        disabled={loading}
        className={`transition-width rounded-full ${style} ${isRecording ? "bg-red-600 w-32" : "w-10"}`}
      >
        <div className="flex justify-center">
          {!isRecording && <FaMicrophone size={25} />}
          {isRecording && <FaStopCircle size={25} />}
          {isRecording && <Timer/>}
        </div>
      </button>
    </>
  );
}

export default RecordButton;

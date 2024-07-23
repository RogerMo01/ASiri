import ChatInput from "./ChatInput";
import ChatHistory from "./ChatHistory";
import { SetStateAction, useEffect, useState } from "react";
import { AxiosHeaders } from "axios";
import { repost } from "./axios_aux";

interface Props{
  showHome: boolean;
  setShowHome: React.Dispatch<SetStateAction<boolean>>;
}

function Chat({showHome, setShowHome}: Props) {
  const [lastUserMessage, setLastUserMessage] = useState("");
  const [lastResponse, setLastResponse] = useState("");
  const [audioURL, setAudioURL] = useState("");
  const [thinking, setThinking] = useState(false);
  const [lastWasAudio, setLastWasAudio] = useState(false);


  ////////////////////// Detect new user text //////////////////////////
  useEffect(() => {
    const fetchResponse = async () => {
      const formData = new FormData();
      formData.append('text', lastUserMessage);

      // Request assistant response
      const server_response = await repost("/text", formData, new AxiosHeaders())

      setLastResponse(server_response);

      console.log(`[*] Server response: ${server_response}`)
      setThinking(false);
    };

    // Actions when request (Audio)
    if (lastUserMessage !== "") {
      fetchResponse();
      setLastResponse("");
      setThinking(true);
      setShowHome(false);
      setLastWasAudio(false);
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [lastUserMessage]);
  ///////////////////////////////////////////////////////////////////////


  ////////////////////// Detect new user audio //////////////////////////
  useEffect(() => {
    const fetchResponse = async () => {
      try{
        // Get audio from URL
        const response = await fetch(audioURL);
        const audioBlob = await response.blob();

        // Create a FormData to send file
        const formData = new FormData();
        formData.append('audio', audioBlob, 'audiofile.mp3'); // Ajusta el nombre del archivo según sea necesario

        // Send audio to server
        const server_response = await repost("/audio", formData, new AxiosHeaders({ 'Content-Type': 'multipart/form-data' }))
        
        setLastResponse(server_response);

        console.log(`[*] Server response: ${server_response}`)
        setThinking(false);

      } catch(error){
        console.error(error)
      }
    };

    // Actions when request (Audio)
    if (audioURL !== ""){
      fetchResponse();
      setLastResponse("");
      setThinking(true);
      setShowHome(false);
      setLastWasAudio(true);
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [audioURL]);
  ///////////////////////////////////////////////////////////////////////

  


  return (
    <div className="flex-col p-4 lg:mx-40 rounded-xl">
      <ChatHistory userMsg={lastUserMessage} assistantMsg={lastResponse} thinking={thinking} showHome={showHome} lastWasAudio={lastWasAudio}/>
      <ChatInput setter={setLastUserMessage} audioURLSetter={setAudioURL} loading={thinking}/>
    </div>
  );
}

export default Chat;

import ChatInput from "./ChatInput";
import ChatHistory from "./ChatHistory";
import { useEffect, useState } from "react";
import { AxiosHeaders } from "axios";
import { repost } from "./axios_aux";


const defaultResponse = "Hey there, I can help you with anything you want, you just give me a touch when you need something from me, I am your assistant in every moment.";

function Chat() {
  const [lastUserMessage, setLastUserMessage] = useState("");
  const [lastResponse, setLastResponse] = useState("");
  const [audioURL, setAudioURL] = useState("");


  ////////////////////// Detect new user text //////////////////////////
  useEffect(() => {
    const fetchResponse = async () => {
      // Temporal displayed response
      setLastResponse("");

      // (DELETE) Simulate wait
      await new Promise(resolve => setTimeout(resolve, 3000));
      
      // Request assistant response
      setLastResponse(defaultResponse);

      console.log(`[*] Server response: ${defaultResponse}`)
    };

    // Actions
    if (lastUserMessage !== "") {
      fetchResponse();
    } else{
      setLastResponse("");
    }
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
        repost("/audio", formData, new AxiosHeaders({ 'Content-Type': 'multipart/form-data' }))

      } catch(error){
        console.error(error)
      }
    };

    // Actions
    if (audioURL !== ""){
      fetchResponse();
    }
  }, [audioURL]);
  ///////////////////////////////////////////////////////////////////////

  


  return (
    <div className="flex-col p-4 lg:mx-40 rounded-xl">
      <ChatHistory userMsg={lastUserMessage} assistantMsg={lastResponse}/>
      <ChatInput setter={setLastUserMessage} audioURLSetter={setAudioURL}/>
    </div>
  );
}

export default Chat;

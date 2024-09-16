// src/hooks/useSpeechSynthesis.ts
import { useEffect, useState } from 'react';

const useSpeechSynthesis = () => {
  const [speaking, setSpeaking] = useState(false);
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
  const [selectedVoice, setSelectedVoice] = useState<SpeechSynthesisVoice | null>(null);

  useEffect(() => {
    const loadVoices = () => {
      const voices = window.speechSynthesis.getVoices();
      setVoices(voices);
      if (voices.length > 0) {
        setSelectedVoice(voices[0]); // Default to the first voice
      }

      // Select 9 as default voice
      try{setSelectedVoice(voices[9]);}catch(e){console.log(e)}
    };

    window.speechSynthesis.onvoiceschanged = loadVoices;
    loadVoices();
  }, []);

  const speak = (text: string) => {
    if (!window.speechSynthesis) {
      alert('Speech Synthesis is not supported for this explorer.');
      return;
    }

    const utterance = new SpeechSynthesisUtterance(text);

    if (selectedVoice) {
      utterance.voice = selectedVoice;
    }

    utterance.onstart = () => setSpeaking(true);
    utterance.onend = () => setSpeaking(false);
    utterance.onerror = () => setSpeaking(false);

    window.speechSynthesis.speak(utterance);
  };

  const cancel = () => {
    if (window.speechSynthesis.speaking) {
      window.speechSynthesis.cancel();
      setSpeaking(false);
    }
  };

  return { speaking, speak, cancel, voices, selectedVoice, setSelectedVoice };
};

export default useSpeechSynthesis;

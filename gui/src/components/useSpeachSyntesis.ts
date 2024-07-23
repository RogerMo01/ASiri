// src/hooks/useSpeechSynthesis.ts
import { useState } from 'react';

const useSpeechSynthesis = () => {
  const [speaking, setSpeaking] = useState(false);

  const speak = (text: string) => {
    if (!window.speechSynthesis) {
      alert('Speech Synthesis is not supported for this explorer.');
      return;
    }

    const utterance = new SpeechSynthesisUtterance(text);

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

  return { speaking, speak, cancel };
};

export default useSpeechSynthesis;

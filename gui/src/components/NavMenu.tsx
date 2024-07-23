import { SetStateAction } from "react";
import "./NavMenu.css";

interface Props{
  setShowHome: React.Dispatch<SetStateAction<boolean>>;
  voices: SpeechSynthesisVoice[];
  selectedVoice: SpeechSynthesisVoice | null;
  setSelectedVoice: React.Dispatch<React.SetStateAction<SpeechSynthesisVoice | null>>;
}

function NavMenu({setShowHome, voices, selectedVoice, setSelectedVoice}: Props) {

  const handleVoiceChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selected = voices.find(voice => voice.name === event.target.value);
    setSelectedVoice(selected || null);
  };

  return (
    <>
      <header className="bg-white mt-0 shadow-2xl">
        <nav
          className="flex items-center justify-center menu-brand p-3 lg:px-8"
          aria-label="Global"
        >
          <div className="flex lg:flex-1 justify-center">
            <a onClick={() => setShowHome(true)} className="-m-1.5 mr-auto cursor-pointer">
              <span className="sr-only">ASiri</span>
              <img className="h-14 w-auto" src="brand.png" alt="ASiri" />
            </a>
            <select className="rounded-2xl border border-gray-300 bg-purple-500 font-semibold px-2 text-white" onChange={handleVoiceChange} value={selectedVoice?.name || ''}>
              {voices.map(voice => (
                <option className="bg-gray-200 text-black font-semibold rounded " key={voice.name} value={voice.name}>
                  {voice.name} ({voice.lang})
                </option>
              ))}
            </select>
          </div>
        </nav>
      </header>
    </>
  );
}

export default NavMenu;

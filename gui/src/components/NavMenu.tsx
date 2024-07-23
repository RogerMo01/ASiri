import { SetStateAction } from "react";
import "./NavMenu.css";

interface Props{
  setShowHome: React.Dispatch<SetStateAction<boolean>>;
}

function NavMenu({setShowHome}: Props) {
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
          </div>
        </nav>
      </header>
    </>
  );
}

export default NavMenu;

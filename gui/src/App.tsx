import "./App.css";
import Chat from "./components/Chat";
import NavMenu from "./components/NavMenu";

function App() {
  return (
    <div className="flex-col">
      <NavMenu/>
      <Chat />
    </div>
  );
}

export default App;

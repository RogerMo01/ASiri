import { FaUser } from "react-icons/fa6";

interface Props{
    msg: string
}

function ChatUserMsg({msg} : Props){
    return(
        <div className="flex m-2 my-6">
            <div className="bg-gray-200 flex-grow border border-gray-300 mx-2 rounded-2xl p-2 text-right">
                <p>{msg}</p>
            </div>
            <div>
                <FaUser className="p-2 bg-sky-400 rounded-3xl" size={45}/>
            </div>
        </div>
    );
}

export default ChatUserMsg;
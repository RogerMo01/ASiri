
interface Props{
    msg: string
}

function ChatAssistantMsg({msg} : Props){
    return(
        <div className="flex m-2 my-6">
            <div className="max-w-12 min-w-12">
                <img src="/logo.png"/>
            </div>
            <div className="bg-gray-200 flex-grow border border-gray-300 mx-2 rounded-2xl p-2 text-left">
                <p>{msg}</p>
            </div>
        </div>
    );
}

export default ChatAssistantMsg;
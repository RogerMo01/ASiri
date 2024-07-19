import axios from "axios";

const serverIP = import.meta.env.VITE_SERVER_IP;
const serverPORT = import.meta.env.VITE_SERVER_PORT;
console.log(`Remote server address: ${serverIP}:${serverPORT}`)

export function request(setter: React.Dispatch<React.SetStateAction<never[]>>) {
    axios.get(`http://${serverIP}:${serverPORT}/api/names`)
    .then((response) => {
        setter(response.data.names);
    })
    .catch((error) => {
        console.error(error);
    });
}


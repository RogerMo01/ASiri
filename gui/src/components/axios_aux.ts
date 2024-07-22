import axios, { AxiosHeaders } from "axios";

const serverIP = import.meta.env.VITE_SERVER_IP;
const serverPORT = import.meta.env.VITE_SERVER_PORT;
console.log(`Remote server address: ${serverIP}:${serverPORT}`)

export function request(endpoint: string, setter: React.Dispatch<React.SetStateAction<never[]>>) {
    axios.get(`http://${serverIP}:${serverPORT}${endpoint}`)
    .then((response) => {
        setter(response.data.names);
    })
    .catch((error) => {
        console.error(error);
    });
}

export function repost(endpoint: string, data: unknown, headers: AxiosHeaders){
    const serverUrl = `http://${serverIP}:${serverPORT}${endpoint}`;
    axios.post(serverUrl, data, {headers: headers})
    .catch((error) => {
        console.error(error);
    });
}

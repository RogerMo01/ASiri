/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from "react";
import { request } from "./request.ts";

function Test() {
  const [data, setData] = useState([]);

  useEffect(() => request(setData), []);

  return (
    <>
      {data.map((item, i) => {
        return <li key={i}>{item}</li>;
      })}
    </>
  );
}

export default Test;

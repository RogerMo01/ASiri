import { useState, useEffect } from 'react';

function Timer() {
  const [startTime] = useState<number>(Date.now());
  const [elapsedTime, setElapsedTime] = useState<number>(0);

  useEffect(() => {
    // Función para actualizar el tiempo transcurrido
    const updateElapsedTime = () => {
      setElapsedTime(Date.now() - startTime);
    };

    // Configurar un intervalo para actualizar el tiempo cada segundo
    const intervalId = setInterval(updateElapsedTime, 75);

    // Limpiar el intervalo cuando el componente se desmonte
    return () => clearInterval(intervalId);
  }, [startTime]);

  // Formatear el tiempo transcurrido en horas, minutos y segundos
  const formatTime = (milliseconds: number) => {
    const totalSeconds = Math.floor(milliseconds / 1000);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    const millisecs = milliseconds % 100;

    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}:${millisecs.toString().padStart(2, '0')}`;
  };

  return (
    <div className='ml-2 font-mono'>
      {formatTime(elapsedTime)}
    </div>
  );
}

export default Timer;

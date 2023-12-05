import React, {useState, useEffect } from "react";
import ReactEcharts from "echarts-for-react"; 
import './App.css';

function App() {
  // useState for setting JS object
  const [data, setdata] = useState({
    signal: [],
    time: [],   
  });

  useEffect(() => {
    fetch("/api/signal")
      .then( res => res.json()
      .then( data => { 
        setdata({
          signal: data.signal,
          time: data.time
        });
      })
    );
  }, []);

  const option = {
    xAxis: {
      type: 'time',
    },
    yAxis: {
      type: 'value',
      min: 'dataMin',
      },
    series: [
      {
        type: 'line',
        data: data.signal,
      }
    ]
  }; 

  return (
    <div>
      <header className = 'header-light'> PRECISION CRYPTO </header>
      <body className='background-dark'>
        <ReactEcharts option={option} />
      </body>
    </div>
  ); 

}

export default App;

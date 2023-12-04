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
      data: data.time
    },
    yAxis: {
      min: Math.min(data.signal),
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
    <ReactEcharts option={option} />
    </div>
  ) 
  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <h1>React and Flask</h1>
  //       {/* Calling data */}
  //       <p>{data.signal}</p>
        
  //     </header>
  //   </div>
  // )
}

export default App;

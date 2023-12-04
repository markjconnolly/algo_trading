import React, {useState, useEffect } from "react";
import ReactEcharts from "echarts-for-react"; 
import './App.css';

function App() {
  // useState for setting JS object
  const [data, setdata] = useState({
    signal: [],   
  });

  // useEffect(() => {
  //   fetch("/api/users/1")
  //     .then( res => res.json()
  //     .then( data => { 
  //       setdata({
  //         name: data.name,
  //         age: data.Age,
  //         date: data.Date,
  //         programming: data.programming}
  //       );
  //     })
  //   );
  // }, []);

  useEffect(() => {
    fetch("/api/signal")
      .then( res => res.json()
      .then( data => { 
        setdata({
          signal: data.signal
        });
        console.log(data.signal)
      })
    );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>React and Flask</h1>
        {/* Calling data */}
        <p>{data.signal}</p>
        
      </header>
    </div>
  )
}

export default App;

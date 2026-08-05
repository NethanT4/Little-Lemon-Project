import { useState } from 'react';  // Import the useState hook from React to manage state in the component
import './App.css';  // Import the CSS file for styling the app

function App() {
  // Initial value of num is set to 0.
  const [num, setNum] = useState(0);

  return (
    // The main container for the app content
    <div className="app-container">
      <h1 className="counter-heading">Current Number: {num}</h1>
      <div className="button-container">
        <button 
          className="counter-button" 
          onClick={() => setNum(num + 1)}  
        >
          Add 1
        </button>
        
     
        <button 
          className="counter-button" 
          onClick={() => setNum(num - 1)}  
        >
          Subtract 1
        </button>
        
      </div>
    </div>
  );
}

export default App;
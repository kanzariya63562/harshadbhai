import React, { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);

  
  useEffect(() => {
    
    document.title = `You clicked ${count} times`;
  });

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );







  


  // The useEffect Hook allows you to perform side effects in your components. Some examples of side effects are: fetching data, directly updating the DOM, and timers.


}





export default App;
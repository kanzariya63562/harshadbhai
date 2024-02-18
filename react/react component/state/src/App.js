// import React from 'react';
// import Profile from './Profile';

// function App() {
//   return (
//     <div >
      
//       <Profile/>
//     </div>
//   );
// }

// export default App;


import React, { useState } from 'react';

function Counter() {
  // Step 2: Declare state variable
  const [count, setCount] = useState(0);

  // Function to handle incrementing count
  const incrementCount = () => {
    // Step 3: Update state using the setCount function
    setCount(count + 1);
  };

  // Function to handle decrementing count
  const decrementCount = () => {
    // Step 3: Update state using the setCount function
    setCount(count - 1);
  };

  return (
    <div>
      <h2>Count: {count}</h2>
      {/* Button to increment count */}
      <button onClick={incrementCount}>Increment</button>
      {/* Button to decrement count */}
      <button onClick={decrementCount}>Decrement</button>
    </div>
  );
}

export default Counter;

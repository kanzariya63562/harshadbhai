import React from 'react';
import Greeting from './Greeting'; // Import the Greeting component

function App() {
  return (
    <div>
      {/* Render the Greeting component and pass the 'name' prop */}
      <Greeting name="John" />
    </div>
  );
}

export default App;

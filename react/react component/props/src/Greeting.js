import React from 'react';

// Functional component named Greeting that accepts props
function Greeting(props) {
  return (
    <div>
      {/* Accessing and displaying the 'name' prop */}
      <h1>Hello, {props.name}!</h1>
    </div>
  );
}

export default Greeting;
import React from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  // Define props to pass to ChildComponent
  const name = "Alice";
  const age = 30;

  return (
    <div>
      {/* Render ChildComponent and pass props */}
      <ChildComponent name={name} age={age} />
    </div>
  );
}

export default ParentComponent;
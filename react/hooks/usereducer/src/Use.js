import React, { useRef } from 'react';

function MyComponent() {
  // Create a ref using the useRef hook
  const inputRef = useRef(null);

  // Function to focus on the input field when a button is clicked
  const focusInput = () => {
    // Access the current value of the ref using inputRef.current
    inputRef.current.focus();
  };

  return (
    <div>
      {/* Input field with ref assigned */}
      <input type="text" ref={inputRef} />

      {/* Button to trigger focus on the input field */}
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}

export default MyComponent;
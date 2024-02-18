

import React, { useRef } from 'react';

function MyForm() {
  
  const nameInputRef = useRef(null);
  const emailInputRef = useRef(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    
    console.log("Name:", nameInputRef.current.value);
    console.log("Email:", emailInputRef.current.value);
  
    event.target.reset();
  };

  return (
    <form onSubmit={handleSubmit}>
      {}
      <label>
        Name:
        <input type="text" ref={nameInputRef} />
      </label>
      <br />
      <label>
        Email:
        <input type="email" ref={emailInputRef} />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}

export default MyForm;
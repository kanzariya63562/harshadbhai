import React, { useState, useMemo } from 'react';

function ExpensiveCalculation({ value }) {
 
  const calculateExpensiveValue = (value) => {
    console.log("Calculating expensive value...");
    return value * 2;
  };

  
  const memoizedValue = useMemo(() => calculateExpensiveValue(value), [value]);

  return (
    <div>
      <p>Original value: {value}</p>
      <p>Expensive value: {memoizedValue}</p>
    </div>
  );
}

function App() {
  const [inputValue, setInputValue] = useState(5);

  return (
    <div>
      <input
        type="number"
        value={inputValue}
        onChange={(e) => setInputValue(parseInt(e.target.value))}
      />
      <ExpensiveCalculation value={inputValue} />
    </div>
  );
}

export default App;
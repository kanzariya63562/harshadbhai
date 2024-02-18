import React, {useState} from 'react';

const App = () => {
  const [data,setData]=useState(0)
  console.warn(data)
  return(
    <div>
      <h2>useState hook {data}</h2>
      <button onClick={()=>setData(data+1)}>updata data</button>
    </div>
  );
};


// useState is React Hook that allows you to add state to a functional component. It returns an array with two values: the current state and a function to update it. The Hook takes an initial state value as an argument and returns an updated state value whenever the setter function is called.

export default App;
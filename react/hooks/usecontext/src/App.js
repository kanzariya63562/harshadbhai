import './App.css';
import React from 'react'
import Child from './Child'
function App() {
  const [count,setCount]=React.useState(0)
  return (
    <div className="App">
      <Child count={count} />
      <button onClick={()=>{setCount( Math.floor(Math.random()*10) )}} >Update Counter</button>
    </div>
  );
}


// The useContext Hook provides function components access to the context value for a context object. It: Takes the context object (i.e., value returned from React. createContext ) as the one argument it accepts. And returns the current context value as given by the nearest context provider.



export default App;
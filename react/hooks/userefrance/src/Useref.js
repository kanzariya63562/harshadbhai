import React ,  {useRef} from 'react';

const hello = () => {



  const luckyName = useRef(null)
  const[shoe, setshow] = useState(false);


  const submitform = () => {
    e.preventDefault();
    const name = luckyName.current.value;
    name = "" ? alert("plz fill the data") : setShow(true);
  }
  return (
    <div>

      <form action="" onsubmit={submitform}>

      <div>
        <label htmlFor="luckyName">enter your luckyname</label>
        <input type="text" id="luckyName" ref={luckyName}></input>
      </div>
      <button>Submit</button>
     
      </form>

      <p>{'show ? your lucky name is ${luckyName.current.value}' : "true"}</p>
     
    
    </div>
  )
}


export default hello;



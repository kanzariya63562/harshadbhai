import React , {useState,useRef} from 'react'

const Uncontrolled = () => {
    const luckyName = useRef(null);
    const[show, setShow] = useState(false);

    const submitForm = (e) => {
        e.preventDefault();
        const name = luckyName.current.value;
        name = "" ? alert("plz fill the data") : setShow(true);
      }

    return (
        <div>
            <form action=" " onsubmit={submitForm}>
                <div>
                <label htmlFor="luckyName">enter your luckyname</label>
                <input type="text" id="luckyName" ref={luckyName}/>
                </div>
                <br/>
                <button>submit</button>

            </form>
            <p> { show ? 'your lucky name is ${luckyName.current.value}' : "true"}</p>
        </div>
    )
}

export default Uncontrolled;
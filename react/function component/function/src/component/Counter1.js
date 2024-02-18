import React, {useEffect} from 'react';





function Counter1({number}){


    useEffect(()=>{
        console.log("FunctionalComponent : Mounting..")


       
    },[number])



     
        return (
        <div>
            <h1>{number}</h1>
        </div>

        );
    

        }

export default Counter1;
import React, {Component} from 'react';
import Counter1 from './component/Counter1';


// A functional component is just a plain JavaScript pure function that accepts props as an argument and returns a React element(JSX). A class component requires you to extend from React. Component and create a render function that returns a React element

class App extends Component {


  constructor(){
    super();

    this.state={
      count:0
    }
  }

  componentDidMount(){

    console.log("componentDidMount : when component render first time")
  }



  increment(){
    this.setState({count : this.state.count + 1 })
  }


  componentWillUnmount(){
    console.log(" componentWillUnmount : component remove")
  }



  render() {
return (
    <div>

      <Counter1 number={this.state.count}></Counter1>
     
      <button onClick={()=>{this.increment()}}>click me</button>
      
    </div>
  );
  }
}

export default App;

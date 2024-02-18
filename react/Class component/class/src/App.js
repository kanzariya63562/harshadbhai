import React, {Component} from 'react';
import Counter from './component/Counter';


class App extends Component {


  constructor(){
    super();

    this.state={
      count:0
    }
  }

  // For a component to be mounted in ReactJS it means to be initialized and inserted in the DOM. Mounting is the initial phase in which the instance of the component is created and inserted into the DOM. When the component gets successfully inserted into the DOM, the component is said to be mounted.
// To display the latest or updated information, and content on the UI after any User interaction or data fetch from the API, we have to update the state of the component. ...
// To update the state of a class based component we will be using the given setState method.
  componentDidMount(){

    console.log("componentDidMount : when component render first time")
  }



  increment(){
    this.setState({count : this.state.count + 1 })
  }



  render() {
return (
    <div>

      <Counter number={this.state.count}></Counter>
     
      <button onClick={()=>{this.increment()}}>click me</button>
      
    </div>
  );
  }
}

export default App;

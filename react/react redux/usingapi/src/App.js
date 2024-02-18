import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CreateForm from './components/CreateForm';
import ReadList from './components/ReadList';
import UpdateForm from './components/UpdateForm';
import DeleteButton from './components/DeleteButton';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/create" component={CreateForm} />
        <Route path="/read" component={ReadList} />
        <Route path="/update/:id" component={UpdateForm} />
        <Route path="/delete/:id" component={DeleteButton} />
      </Switch>
    </Router>
  );
};

export default App;
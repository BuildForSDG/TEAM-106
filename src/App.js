import React from 'react';
import './App.css';

import { Route, Switch } from "react-router-dom";

// import the component parts
import Home from './components/Home/Home';
import NotFound from './components/NotFound/NotFound';


function App() {
  return (
    <Switch>
		<Route path="/" exact component={Home} />
		<Route component={ NotFound } />
	</Switch>
  );
}

export default App;

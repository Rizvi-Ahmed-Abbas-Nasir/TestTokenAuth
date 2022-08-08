import './App.css';
import { ToastContainer } from "react-toastify";
import React, { Component } from "react";
import Root from "./Root";
import { Route, Switch } from "react-router-dom";
import SignUp from './components/signup/SignUp';
import Home from './Home';

import axios from "axios";

if (window.location.origin === "http://localhost:3000") {
  axios.defaults.baseURL = "http://127.0.0.1:8000";
} else {
  axios.defaults.baseURL = window.location.origin;
}

class App extends Component {
  render() {
    return (
      <div>
        <Root>
          <ToastContainer hideProgressBar={true} newestOnTop={true} />
          <Switch>
          <Route path="/signup" component={SignUp} />
          <Route exact path="/" component={Home} />
          </Switch>
        </Root>
      </div>
    );
  }
}

export default App;

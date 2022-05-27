import React from 'react';
import {BrowserRouter as Router, Switch,Route} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

import AddTodo from './components/add-todo';
import TodosList from './components/todos-list';
import Login from './components/login';
import Signup from './components/signup';
import Header from './components/nav-bar';

import Product from './components/product';

import TodoDataService from './services/todos';

function App(){
  const [user, setUser] = React.useState(null);
  const [token, setToken] = React.useState(null);
  const [error, setError] = React.useState('');

  async function login(user = null){
    TodoDataService.login(user)
      .then(response => {
        setToken(response.data.token);
        setUser(user.username);
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', user.username);
        setError('');
      })
      .catch( e => {
        console.log('login', e);
        setError(e.toString());
      });
  }

  async function logout(){
    setToken("");
    setUser("");
    localStorage.setItem('token','');
    localStorage.setItem('user', '');
  }

  async function signup(user = null){
    TodoDataService.signup(user)
      .then( response => {
        setToken(response.data.token);
        setUser(user.username);
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', user.username);
      })
      .catch( e=>{
        console.log(e);
        setError(e.toString());
      })
  }

  return (
    <div className="App">
      <Router>
        <Header user={user} logout={logout} />

        <div>
          
            <Switch>
              <Route exact path={["/", "/todos"]} render={(props)=><TodosList {...props} token={token} />}></Route>
              <Route path="/todos/create" render={(props)=><AddTodo {...props} token={token} />}></Route>
              <Route path="/todos/:id" render={(props)=><AddTodo {...props} token={token}/>}></Route>
              <Route path="/login" render={(props)=><Login {...props} login={login} />}></Route>
              <Route path="/signup" render={(props)=><Signup {...props} signup={signup} />}></Route>
              <Route path="/products" render={(props)=><Product {...props} token={token} />}></Route>
            </Switch>
          
        </div>
      </Router>

      <footer className="text-center text-lg-start bg-light text-muted mt-4">
        <div className="text-center p-4">
          Copyright - <a target="_blank" rel="noreferrer" className="text-reset fw-bold text-decoration-none" href="https://twitter.com/MarcoTulio_Ruiz">
            Marco Tulio Ruiz
          </a>
        </div>
      </footer>
    </div>
  );
}

export default App;

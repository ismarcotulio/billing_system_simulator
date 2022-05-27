import React from 'react';

import {Link} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';

export default function Header(props){

    console.log(props);

    return (
        <Navbar bg="primary" variant="dark">
          <div className="container-fluid">
            <Navbar.Brand>FarMarco's Web</Navbar.Brand>
            <Nav className="me-auto">
              <Container>
                <Link className="nav-link" to="/products">Productos</Link>
                { props.user ? (
                  <Link className="nav-link" to="/#" onClick={props.logout}>Logout ({props.user})</Link>
                ) : (
                  <>
                    <Link className="nav-link" to="/login">Login</Link>
                    <Link className="nav-link" to="/signup">Sign Up</Link>
                  </>
                )}  
              </Container>  
            </Nav>
          </div>
        </Navbar>
    )

}
import React from 'react';
import {Navbar, Button, Nav } from 'react-bootstrap';
import {  NavLink } from "react-router-dom";


const navItems = [
  {
    id: "1",
    title: "About",
    path: "about",
  },
  {
    id: "2",
    title: "Services",
    path: "services",
  },
  {
    id: "3",
    title: "Contact",
    path: "contact",
  },
  {
    id: "4",
    title: "Signup",
    path: "signup",
  },
]

const NavigationBar = (props) => {
  
  return(
       <Navbar collapseOnSelect expand="lg" bg="light" variant="light" 
        className="font-weight-bold d-flex align-items-center">
        <Navbar.Brand as={NavLink} to="/">
          <img
            alt=""
            src="/logo.svg"
            width="30"
            height="30"
            className="d-inline-block align-top"
          />{' '}
          DevData
        </Navbar.Brand>

        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav" className="justify-content-end">
          <Nav >
            {navItems.map(i => 
              <Nav.Item className="m-3">
                 { i.id === '4'?
                  <NavLink exact
                    href="/"
                    key={i.id} 
                    className="mx-3 btn btn-outline-info text-dark"
                    eventKey={i.path}
                    as={Button}
                    to={i.path} 
                    activeStyle={{color: "cyan"}}
                    >
                    {i.title}
                  </NavLink>
                  :
                  <NavLink exact
                  href="/"
                  key={i.id} 
                  className="mx-3 text-dark"
                  eventKey={i.path}
                  as={NavLink}
                  to={i.path} 
                  activeStyle={{color: "cyan"}}
                  >
                    {i.title}
                  </NavLink>
                }
              </Nav.Item>
            )}
          </Nav>
        </Navbar.Collapse>
      </Navbar>
  )
}

export default NavigationBar;



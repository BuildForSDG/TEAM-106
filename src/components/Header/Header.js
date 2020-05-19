import React from 'react';
import './Header.css';
import { Button } from 'react-bootstrap';

// import the navbar
import NavigationBar from '../navigationbar/navigationbar';

// create a Header component
const Header = (props) => {
	return(
		<div className="">
			<NavigationBar />
			<div className="app head mx-auto">
			  <h1 className="">Welcome To Dev Data</h1>
			  <h5 className="text-capitalize"> Real Time Developer Data across the Globe </h5>
			  <p>
			    <Button variant="info">Learn more</Button>
			  </p>
			</div> 
		</div>
	)
}

// export the header
export default Header;
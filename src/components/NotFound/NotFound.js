import React from "react";
import "./NotFound.css";
import Navigationbar from '../navigationbar/navigationbar';

export default () =>
  <div>
	<Navigationbar  />
  	<div className="NotFound ">
	    <h3>Sorry, page not found!</h3>
	</div>
  </div>;
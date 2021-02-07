import React from 'react'
//import mylogo from "./images/mpoyi.jpg";



function Navbar() {
    return (
        
    <nav className="navbar navbar-expand-lg navbar-light fixed-top ">

    <div className="container">
        <a className="navbar-brand " href="#">ruth catering</a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            
            <i className="fa fa-bars"></i>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">

            <ul className="navbar-nav ml-auto">
                <li className="nav-item ">
                    <a className="nav-link" href="#">Home </a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">About</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">service</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link " href="#">Contact-us</a>
                </li>
            </ul>
        </div>

    </div>
</nav>

    )
}

export default Navbar

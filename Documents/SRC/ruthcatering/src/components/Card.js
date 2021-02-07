import React from 'react'
import mylogo from "../images/cover.jpg";



function Card() {
    return (
        
    <div className="container-fluid padding p-5">
        <h1 className="text-center">MEET OUR CHEFS</h1>
        <div className="row padding">
            <div className="col-md-4">
                <div className="card">
                        <img src={mylogo} alt="" className="card-img-top" />
                    <div className="card-body">
                        <h4 className="card-title text-center">Chef Siki</h4>
                        <p className="card-text text-center text-center">Still wait </p>
                    </div>
                </div>
            </div>

            <div className="col-md-4">
                <div className="card">
                    <img src={mylogo} alt="" className="card-img-top" />
            
                    <div className="card-body">
                        <h4 className="card-title text-center">Chef Ruth</h4>
                        <p className="card-text text-center">OWNER & MANAGER</p>

                    </div>
                </div>
            </div>

            <div className="col-md-4">
                <div className="card">
                    <img src={mylogo} alt="" className="card-img-top" /> 
                    <div className="card-body">
                        <h4 className="card-title text-center">Chef Flora</h4>
                        <p className="card-text text-center">PASTRY KITCHEN</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    )
}

export default Card

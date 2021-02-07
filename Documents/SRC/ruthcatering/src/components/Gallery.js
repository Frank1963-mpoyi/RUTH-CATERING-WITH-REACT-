import React from 'react'
import mylogo from "../images/food3.jpg";
import logo from "../images/drink (1).jpg";
import drink1 from "../images/drink (2).jpg";
import food2 from "../images/food2.jpg";
import drink2 from "../images/drink (4).jpg";
import drink3 from "../images/food5.jpg";
import drink4 from "../images/food4.jpg";
import drink5 from "../images/food2.jpg";

function Gallery() {
    return (
        <section id="gallery">
        <div>
            <h2 class="title-text">Main Cuisines</h2>
        </div>

        <div id="gallery-centre">
            <article class="gallery-item d-none d-md-block  ">
                <a href="">
                    <img class="" src={mylogo} alt="" />
                </a>
            </article>

            <article class="gallery-item">
                <a href="">
                    <img src={logo} alt="" />
                </a>
            </article>

            <article class="gallery-item">
                <a href="">
                    <img src={drink1} alt="" />
                </a>
            </article>

            <article class="gallery-item">
                <a href="">
                    <img src={food2} alt="" />
                </a>
            </article>

            <article class="gallery-item">
                <a href="">
                    <img src={drink2} alt="" />
                </a>
            </article>

            <article class="gallery-item d-none d-md-block ">
                <a href="">
                    <img src={drink3} alt="" />
                </a>
            </article>

            <article class="gallery-item d-none d-md-block ">
                <a href="">
                    <img src={drink4} alt="" />
                </a>
            </article>

            <article class="gallery-item  d-none d-md-block ">
                <a href="">
                    <img src={drink5} alt="" />
                </a>
            </article>
        </div>

    </section>
    )
}

export default Gallery

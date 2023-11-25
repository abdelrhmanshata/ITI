//////////////////////////////////////////////////
// Database 
// Slider Images
var images = [
    "../images/about/image1.jpg",
    "../images/about/image2.jpg",
    "../images/about/image3.jpg"
];
/////////////////////////
// Image Slider
var index = 0;
var image = document.getElementById("imageSlider");
var dotsContanir = document.getElementById("dots");
function createDots() {
    for (var i = 0; i < images.length; i++) {
        var dot = document.createElement("span");
        dot.className = "dot";
        dotsContanir.appendChild(dot);
    }
}
///////////////
var dots = document.getElementsByClassName("dot");
function selectedDot(index) {
    for (var i = 0; i < dots.length; i++) {
        if (i == index) {
            dots[i].style.backgroundColor = "#db4444";
        } else {
            dots[i].style.backgroundColor = "#bbb";
        }
    }
}
function next() {
    index += 1;
    if (index == images.length)
        index = 0;
    image.setAttribute("src", images[index % images.length]);
    selectedDot(index);
}
var interval;
function autoPlay() {
    interval = setInterval(next, 5000);
}

//////////////////////////////////////////////////
// Calling Function
// Creates a Dot Of Sliders and select index 0 defult
createDots();
selectedDot(0);
// autoPlaySlider 
autoPlay()


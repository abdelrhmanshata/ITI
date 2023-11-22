// 
var favorite = document.getElementById("favorite");
favorite.onmouseover = function () {
    favorite.innerHTML = "favorite";
}
favorite.onmouseout = function () {
    favorite.innerHTML = "favorite_border";
}

favorite.onclick = function () {
    alert("favorite");
};


// Image Slider

var image = document.getElementById("image");
var dotsContanir = document.getElementById("dots");


var index = 0;
var images = [
    "../images/sliderImage1.jpg",
    "../images/sliderImage2.jpg",
    "../images/sliderImage3.jpg", 
    "../images/sliderImage4.jpg", 
    "../images/sliderImage5.jpg"
];

function createDots() {

    for (var i = 0; i < images.length; i++) {
        var dot = document.createElement("span");
        dot.className = "dot";
        dotsContanir.appendChild(dot);
    }
}
createDots();

var dots = document.getElementsByClassName("dot");

function selectedDot(index){
    for (var i = 0; i < dots.length; i++) {
        if(i==index) {
            dots[i].style.backgroundColor ="#db4444";
        }else{
            dots[i].style.backgroundColor ="#bbb";
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

function previous() {
    index -= 1;
    if (index < 0)
        index = images.length - 1
    image.setAttribute("src", images[index % images.length]);
    selectedDot(index);
}

var interval;
function autoPlay() {
    interval = setInterval(next, 3000);
}

autoPlay()






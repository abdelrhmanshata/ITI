var index = 0;
var images = ["./images/image1.jpeg", "./images/image2.jpeg", "./images/image3.jpeg", "./images/image4.jpeg"];

var image = document.getElementById("image");

function next() {
    index += 1;
    if (index == images.length)
        index = 0;
    console.log(index);
    image.setAttribute("src", images[index % images.length]);
}

function previous() {
    index -= 1;
    if (index < 0)
        index = images.length-1
    console.log(index);
    image.setAttribute("src", images[index % images.length]);
}

var playBtn = document.getElementById("playBtn");
var stopBtn = document.getElementById("stopBtn");
var interval;

function autoPlay() {
    interval = setInterval(next, 1000);
    playBtn.removeEventListener('click', autoPlay);
    stopBtn.addEventListener('click',stopPlay);
}

function stopPlay() {
    clearInterval(interval);
    playBtn.addEventListener('click', autoPlay);
    stopBtn.removeEventListener('click',stopPlay);
}

playBtn.addEventListener('click', autoPlay);


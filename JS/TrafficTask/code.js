var input = document.getElementById("inputNum");
var lights = document.getElementsByClassName("light");
function lightOn() {
    if (input.value == "1") {
        lights[0].style.background = "red";
    } else if (input.value == "2") {
        lights[1].style.background = "yellow";
    } else if (input.value == "3") {
        lights[2].style.background = "lawngreen";
    } else {
        lights[0].style.background = "gray";
        lights[1].style.background = "gray";
        lights[2].style.background = "gray";
    }
}

var playBtn = document.getElementById("playBtn");
var stopBtn = document.getElementById("stopBtn");
var interval;

function autoPlay() {
    var index = 0;
    interval = setInterval(function () {
        if (index % 3 == 0) {
            lights[0].style.background = "red";
            lights[1].style.background = "gray";
            lights[2].style.background = "gray";
        } else if (index % 3 == 1) {
            lights[0].style.background = "gray";
            lights[1].style.background = "yellow";
            lights[2].style.background = "gray";
        }
        else if (index % 3 == 2) {
            lights[0].style.background = "gray";
            lights[1].style.background = "gray";
            lights[2].style.background = "lawngreen";
        }
        input.value=index % 3 +1;
        index++;
    }, 1000);

    playBtn.removeEventListener('click', autoPlay);
    stopBtn.addEventListener('click',stopPlay);
}

function stopPlay() {
    clearInterval(interval);
    playBtn.addEventListener('click', autoPlay);
    stopBtn.removeEventListener('click',stopPlay);
}

playBtn.addEventListener('click', autoPlay);
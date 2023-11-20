var inputTags = document.getElementById("inputTags");
var inputColor = document.getElementById("inputColor");
var inputText = document.getElementById("inputText");

var circleColor = document.getElementById("circleColor");

var container = document.getElementById("container");

function selectColor() {
    circleColor.style.background = inputColor.value;
}

function create() {
    if (inputTags.value.length != 0 && inputColor.value.length != 0 && inputText.value.length != 0) {
        var element = document.createElement(inputTags.value);
        element.style.background = inputColor.value;
        element.style.width = "100%";
        element.style.height = "20px";
        var text = document.createTextNode(`${inputText.value}`);
        element.appendChild(text);
        var result = container.appendChild(element);
        console.log(result);
    }
    else {
        console.log("Please Enter a value");
    }
}
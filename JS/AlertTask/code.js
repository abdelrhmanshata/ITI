var SuccessButton = document.getElementById("SuccessButton");
var SuccessAlert = document.getElementById("SuccessAlert");

var ErrorButton = document.getElementById("ErrorButton");
var ErrorAlert = document.getElementById("ErrorAlert");

SuccessButton.onclick = function () {
    SuccessAlert.style.display = "flex";
    ErrorAlert.style.display = "none";
}
ErrorButton.onclick = function () {
    SuccessAlert.style.display = "none";
    ErrorAlert.style.display = "flex";
}
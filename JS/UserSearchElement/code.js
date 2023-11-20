var msgTagName = document.getElementById("msgTagName");
var inputTagName = document.getElementById("inputTagName");

var msgClassName = document.getElementById("msgClassName");
var inputClassName = document.getElementById("inputClassName");

var msgID = document.getElementById("msgID");
var inputID = document.getElementById("inputID");

var msgName = document.getElementById("msgName");
var inputName = document.getElementById("inputName");

var result = document.getElementById("result");

var countTagName = 0, countClassName = 0, countName = 0;
var isIDFound = false;
function showResult() {

    var elements = document.querySelectorAll('div.Container *');

    if (inputTagName.value.length == 0) {
        msgTagName.style.visibility = "visible";
        return;
    } else {
        msgTagName.style.visibility = "hidden";
    }
    if (inputClassName.value.length == 0) {
        msgClassName.style.visibility = "visible";
        return;
    } else {
        msgClassName.style.visibility = "hidden";
    }
    if (inputID.value.length == 0) {
        msgID.style.visibility = "visible";
        return;
    } else {
        msgID.style.visibility = "hidden";
    }
    if (inputName.value.length == 0) {
        msgName.style.visibility = "visible";
        return;
    } else {
        msgName.style.visibility = "hidden";
    }

    var isFound = document.getElementById(inputID.value);
    isIDFound = isFound == null ? false : true;

    // var elements = document.querySelectorAll('div.Container *');
    var elements = document.querySelectorAll('*');
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].tagName == inputTagName.value.toUpperCase()) {
            countTagName++;
        }
        if (elements[i].className == inputClassName.value) {
            countClassName++;
            console.log(elements[i].className);
        }
        if (elements[i].name == inputName.value) {
            countName++;
            console.log(elements[i].name);
        }
    }

    result.innerHTML=`Tag ${countTagName} || Class ${countClassName} || ID ${isIDFound} || Name ${countName}`;
}
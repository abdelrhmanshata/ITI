var userName = document.getElementById("name");
var userEmail = document.getElementById("email");
var userPassword = document.getElementById("password");

var Genders = document.getElementsByName('Gender');
var Sports = document.getElementsByName('fav_Sports');

var country = document.getElementById("country");

var SubmitBtn = document.getElementById("Submit");
var ResetBtn = document.getElementById("Reset");

var msg = document.getElementsByTagName("p");

country.onchange = function (event) {
    if (event.target.value.length == 0) {
        country.style.border = "1px solid red"
    } else {
        country.style.border = "1px solid green"
    }
};


function getGender(Genders) {
    for (var i = 0; i < Genders.length; i++) {
        if (Genders[i].checked) {
            return Genders[i].value;
        }
    }
    return null;
}

function getSport(Sports) {
    var Sport = [];
    for (var i = 0; i < Sports.length; i++) {
        if (Sports[i].checked) {
            Sport.push(Sports[i].value);
        }
    }
    return Sport;
}

userName.oninput = function (event) {
    if (event.target.value.length == 0) {
        userName.style.border = "1px solid red"
    } else {
        userName.style.border = "1px solid green"
    }
}

function isValidEmail(email) {
    const emailRegex = /^[a-zA-Z]+[a-zA-Z0-9]*@[a-zA-Z]+\.[a-zA-Z]+$/;
    return emailRegex.test(email);
}

userEmail.oninput = function () {
    if (!isValidEmail(userEmail.value)) {
        userEmail.style.border = "1px solid red";
    } else {
        userEmail.style.border = "1px solid green";
    }
}

userPassword.oninput = function (event) {
    if (event.target.value.length < 8) {
        userPassword.style.border = "1px solid red"
    } else {
        userPassword.style.border = "1px solid green"
    }
}

function Submit() {

    if (userName.value.length == 0) {
        console.log("Please enter user name");
        msg[0].style.display = "block";
        return;
    } else {
        msg[0].style.display = "none";
    }

    if (!isValidEmail(userEmail.value)) {
        console.log("Please enter valid Email");
        msg[1].style.display = "block";
        return;
    } else {
        msg[1].style.display = "none";
    }

    if (userPassword.value.length < 8) {
        console.log("Password must be 8chars at least");
        msg[2].style.display = "block";
        return;
    } else {
        msg[2].style.display = "none";
    }

    if (getGender(Genders) == null) {
        console.log("Please select your gender");
        msg[3].style.display = "block";
        return;
    } else {
        msg[3].style.display = "none";
    }

    if (getSport(Sports).length < 2) {
        console.log("Please select at least two Sports");
        msg[4].style.display = "block";
        return;
    } else {
        msg[4].style.display = "none";
    }

    if (country.value.length == 0) {
        console.log("Please select your country");
        msg[5].style.display = "block";
        return;
    } else {
        msg[5].style.display = "none";
    }


    alert(`User Name:${userName.value} Email:${userEmail.value} Password:${userPassword.value} \n` + `Gender:${getGender(Genders)} Sports:${getSport(Sports)} Country:${country.value}`);
}

function Reset() {
    userName.value = "";
    userEmail.value = "";
    userPassword.value = "";
    Genders.forEach(element => element.checked = false);
    Sports.forEach(element => element.checked = false);
    country.options[0].selected = true;

    userName.style.border = "1px solid red";
    userEmail.style.border = "1px solid red";
    userPassword.style.border = "1px solid red";
    country.style.border = "1px solid red"

    for (var i = 0; i < msg.length; i++) {
        msg[i].style.display = "none";
    }

}




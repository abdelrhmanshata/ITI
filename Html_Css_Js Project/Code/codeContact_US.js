//////////////////////////////////////////////////

function isValidName(name) {
    const nameRegex = /^[a-zA-Z][a-zA-Z0-9]*/;
    return nameRegex.test(name);
}

function isValidEmail(email) {
    const emailRegex = /^[a-zA-Z]+[a-zA-Z0-9]*@[a-zA-Z]+\.[a-zA-Z]+$/;
    return emailRegex.test(email);
}
function isValidPhone(phone) {
    const mobileRegex = /^(010|011|012|015)\d{8}$/;
    return mobileRegex.test(phone);
}

// 

var sendMassage = document.getElementById("sendMassage");
var userName = document.getElementById("userName");
userName.oninput = function (event) {
    if (userName.value.length == 0) {
        userName.style.border = "1px solid red";
    } else {
        userName.style.border = "1px solid green";
    }
}

var userEmail = document.getElementById("userEmail");
userEmail.oninput = function (event) {
    if (userEmail.value.length == 0 || !isValidEmail(userEmail.value)) {
        userEmail.style.border = "1px solid red";
    } else {
        userEmail.style.border = "1px solid green";
    }
}

var userPhone = document.getElementById("userPhone");
userPhone.oninput = function (event) {
    if (userPhone.value.length == 0 || !isValidPhone(userPhone.value)) {
        userPhone.style.border = "1px solid red";
    } else {
        userPhone.style.border = "1px solid green";
    }
}

var userMassage = document.getElementById("userMassage");
userMassage.oninput = function (event) {
    if (userMassage.value.length == 0) {
        userMassage.style.border = "1px solid red";
    } else {
        userMassage.style.border = "1px solid green";
    }
}

sendMassage.onclick = function () {

    if (userName.value.length == 0) {
        userName.style.border = "1px solid red";
        userName.setAttribute("placeholder", "* Name is required");
        return;
    }

    if (!isValidName(userName.value)) {
        userName.style.border = "1px solid red";
        userName.setAttribute("placeholder", "* Please Enter Valid Name");
        return;
    }

    if (userEmail.value.length == 0) {
        userEmail.style.border = "1px solid red";
        userEmail.setAttribute("placeholder", "* Email is required");
        return;
    }

    if (!isValidEmail(userEmail.value)) {
        userEmail.style.border = "1px solid red";
        userEmail.setAttribute("placeholder", "* Please Enter Valid Email");
        return;
    }

    if (userPhone.value.length == 0) {
        userPhone.style.border = "1px solid red";
        userPhone.setAttribute("placeholder", "* Phone is required");
        return;
    }

    if (!isValidPhone(userPhone.value)) {
        userPhone.style.border = "1px solid red";
        userPhone.setAttribute("placeholder", "* Please Enter Valid Phone Number");
        return;
    }

    if (userMassage.value.length == 0) {
        userPhone.style.border = "1px solid red";
        userPhone.setAttribute("placeholder", "* Phone is required");
        return;
    }


    console.log(userName.value, userEmail.value, userPhone.value, userMassage.value);


    // window.open(`mailto:abdelrhmanmohamedshata@gmail.com?subject=Rate the site&body=${userMassage}`);
}
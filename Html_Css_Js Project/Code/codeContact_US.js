//////////////////////////////////////////////////
function isValidEmail(email) {
    const emailRegex = /^[a-zA-Z]+[a-zA-Z0-9]*@[a-zA-Z]+\.[a-zA-Z]+$/;
    return emailRegex.test(email);
}
function isValidPhone(phone) {
    const mobileRegex = /^(010|011|012|015)\d{8}$/;
    return mobileRegex.test(phone);
}

// 
var myForm = document.getElementById("myForm");
var errorMsgs = document.getElementsByClassName("errorMsg");

var userName = document.getElementById("userName");
function validationName() {
    if (userName.value.length == 0) {
        userName.style.border = "1px solid red";
        errorMsgs[0].style.visibility = "visible";
        errorMsgs[0].innerHTML = "* Name is required";
        userName.setAttribute("placeholder", "* Name is required");
        return true;
    } else {
        userName.style.border = "1px solid green";
        errorMsgs[0].style.visibility = "hidden";
        return false;
    }
}
userName.oninput = validationName;
////////////////////////////
var userEmail = document.getElementById("userEmail");
function validationEmail() {
    if (userEmail.value.length == 0) {
        userEmail.style.border = "1px solid red";
        errorMsgs[1].style.visibility = "visible";
        errorMsgs[1].innerHTML = "* Email is required";
        userEmail.setAttribute("placeholder", "* Email is required");
        return true;
    } else if (!isValidEmail(userEmail.value)) {
        userEmail.style.border = "1px solid red";
        errorMsgs[1].style.visibility = "visible";
        errorMsgs[1].innerHTML = "* Please Enter Valid Email";
        userEmail.setAttribute("placeholder", "* Please Enter Valid Email");
        return true;
    } else {
        userEmail.style.border = "1px solid green";
        errorMsgs[1].style.visibility = "hidden";
        return false;
    }
}
userEmail.oninput = validationEmail;
////////////////////////////
var userPhone = document.getElementById("userPhone");
function validationPhone() {
    if (userPhone.value.length == 0) {
        userPhone.style.border = "1px solid red";
        errorMsgs[2].style.visibility = "visible";
        errorMsgs[2].innerHTML = "* Phone is required";
        userPhone.setAttribute("placeholder", "* Phone is required");
        return true;
    } else if (!isValidPhone(userPhone.value)) {
        userPhone.style.border = "1px solid red";
        errorMsgs[2].style.visibility = "visible";
        errorMsgs[2].innerHTML = "* Please Enter Valid Phone";
        userPhone.setAttribute("placeholder", "* Please Enter Valid Phone");
        return true;
    } else {
        userPhone.style.border = "1px solid green";
        errorMsgs[2].style.visibility = "hidden";
        return false;
    }
}
userPhone.oninput = validationPhone;
////////////////////////////
var userMassage = document.getElementById("userMassage");
function validationMassage() {
    if (userMassage.value.length == 0) {
        userMassage.style.border = "1px solid red";
        errorMsgs[3].style.visibility = "visible";
        errorMsgs[3].innerHTML = "* Massage is required";
        userMassage.setAttribute("placeholder", "* Massage is required");
        return true;
    } else {
        userMassage.style.border = "1px solid green";
        errorMsgs[3].style.visibility = "hidden";
        return false;
    }
}
userMassage.oninput = validationMassage;
////////////////////////////

myForm.addEventListener('submit', function (event) {
    event.preventDefault();

    if (validationName())
        return;
    if (validationEmail())
        return;
    if (validationPhone())
        return;
    if (validationMassage())
        return;

    var alertMsg = `Dear ${userName.value},
        Thank you for contacting us
        We will try to respond to you as soon as possible via 
        email : ${userEmail.value} 
        phone : ${userPhone.value}
    Thank you for using our site
    `;
    alert(alertMsg);

    userName.value = "";
    userEmail.value = "";
    userPhone.value = "";
    userMassage.value = "";

    userName.setAttribute("placeholder", "*Your Name");
    userEmail.setAttribute("placeholder", "Your Email");
    userPhone.setAttribute("placeholder", "Your Phone");
    userMassage.setAttribute("placeholder", "Your Massages");
});
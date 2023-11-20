var msgName = document.getElementById("msgName");
var studentName = document.getElementById("studentName");
var msgAge = document.getElementById("msgAge");
var studentAge = document.getElementById("studentAge");

var studentTable = document.getElementById("studentTable");

var ID = 1;
function addStudent() {

    if (studentName.value.length == 0) {
        msgName.innerHTML = "Name is Required";
        msgName.style.visibility = "visible";
        return;
    } else if (studentName.value.length < 3) {
        msgName.innerHTML = "Student Name Must > 3";
        msgName.style.visibility = "visible";
        return;
    } else {
        msgName.style.visibility = "hidden";
    }

    if (studentAge.value.length == 0) {
        msgAge.innerHTML = "Age is Required";
        msgAge.style.visibility = "visible";
        return;
    } else if (studentAge.value <= 18) {
        msgAge.innerHTML = "Student Age Must > 18";
        msgAge.style.visibility = "visible";
        return;
    } else {
        msgAge.style.visibility = "hidden";
    }

    var divStudentRow = document.createElement("div");
    divStudentRow.id = "row_" + ID;

    var pStudentID = document.createElement("p");
    pStudentID.innerHTML = ID++;

    var pStudentName = document.createElement("p");
    pStudentName.innerHTML = studentName.value;

    var pStudentAge = document.createElement("p");
    pStudentAge.innerHTML = studentAge.value;

    var buttonDelete = document.createElement("button");
    buttonDelete.innerHTML = "Delete";
    buttonDelete.onclick = function () {
        const element = document.getElementById("row_" + pStudentID.innerHTML);
        element.remove();
    }

    divStudentRow.append(pStudentID, pStudentName, pStudentAge, buttonDelete);

    studentTable.append(divStudentRow)

}
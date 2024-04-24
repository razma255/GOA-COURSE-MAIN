function infoJoin(firstName, lastName, age, residence, hobby) {
    return "My name is " + firstName + " " + lastName + ". I am " + age + " years old and I live in " + residence + ". My hobby is " + hobby + ".";
}

function ageCheck(age) {
    if (age > 18) {
        console.log("The age is greater than 18.");
    } else if (age < 18) {
        console.log("The age is less than 18.");
    } else {
        console.log("The age is 18.");
    }
}

function alerter() {
    alert("Clicked");
}

function colorChanger() {
    document.getElementById("text").style.color = "green";
}

function changeTextColor() {
    var paragraphs = document.getElementsByTagName("p");
    for (var i = 0; i < paragraphs.length; i++) {
        paragraphs[i].style.color = "blue";
    }
}

window.onload = changeTextColor;

document.getElementById("clickButton").addEventListener("click", alerter);

document.getElementById("colorButton").addEventListener("click", colorChanger);

console.log(infoJoin("John", "Doe", 25, "New York", "Playing guitar"));
ageCheck(20); 
ageCheck(15); 
ageCheck(18); 

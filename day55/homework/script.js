   // Task 1
   function performOperations() {
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);

    var addition = num1 + num2;
    var subtraction = num1 - num2;
    var multiplication = num1 * num2;
    var division = num1 / num2;

    document.getElementById("result").innerText = `Addition: ${addition}, Subtraction: ${subtraction}, Multiplication: ${multiplication}, Division: ${division}`;
}

// Task 2
function submitForm(event) {
    event.preventDefault();
    var inputs = document.getElementsByTagName("input");
    for (var i = 0; i < inputs.length; i++) {
        console.log(inputs[i].value);
    }
}

// Task 3
function displayText() {
    var text = document.getElementById("textInput").value;
    var color = document.getElementById("colorInput").value;
    var displayParagraph = document.getElementById("displayParagraph");

    displayParagraph.innerText = text;
    displayParagraph.style.color = color;
}
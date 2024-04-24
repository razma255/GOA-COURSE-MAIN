function multiplication(num1 , num2 , num3){
    console.log(num1* num2*num3)
}

multiplication( 3123456789, 5 , 5)





function fullNames(firstName, lastName) {
    return firstName + ' ' + lastName;
}

var fullName = concatenateNames('sandro', 'razmadze');
console.log(fullName); 




function addition(num1, num2) {
    return num1 + num2;
}

function subtraction(num1, num2) {
    return num1 - num2;
}

function division(num1, num2) {
    if (num2 === 0) {
        return "Cannot divide by zero";
    } else {
        return num1 / num2;
    }
}

function multiplication(num1, num2) {
    return num1 * num2;
}

var randomNumber1 = Math.floor(Math.random() * 100); 
var randomNumber2 = Math.floor(Math.random() * 100); 

console.log("Addition:", addition(randomNumber1, randomNumber2));

console.log("Subtraction:", subtraction(randomNumber1, randomNumber2));

console.log("Division:", division(randomNumber1, randomNumber2));

console.log("Multiplication:", multiplication(randomNumber1, randomNumber2));




function calculateRectangle(length, width) {
    var perimeter = 2 * (length + width);

    var area = length * width;

    console.log("Perimeter:", perimeter);
    console.log("Area:", area);

    return {
        length: length,
        width: width
    };
}

// Example usage:
var rectangle = calculateRectangle(5, 8);
console.log("Length:", rectangle.length);
console.log("Width:", rectangle.width);

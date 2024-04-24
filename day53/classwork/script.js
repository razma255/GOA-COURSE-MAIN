const firstParagraph = document.getElementById('first');
const lastParagraph = document.getElementById('last');

console.log('First paragraph:', firstParagraph.textContent);
console.log('Last paragraph:', lastParagraph.textContent);

const myInfo = {
    name: 'sandro',
    age: 5,
    favoriteColor: 'Blue'
};

const friendInfo = {
    name: 'data',
    age: 6,
    favoriteColor: 'Green'
};

console.log("My Info:", myInfo);
console.log("Friend's Info:", friendInfo);

function swapText() {
    let firstParagraph = document.getElementById("firstParagraph");
    let secondParagraph = document.getElementById("secondParagraph");
    
    let temp = firstParagraph.textContent;
    
    firstParagraph.textContent = secondParagraph.textContent;
    secondParagraph.textContent = temp;
}



function task1() {
    function addition(x, y) {
        return x + y;
    }

    function multiplication(x, y) {
        return x * y;
    }

    console.log("Addition result:", addition(5, 3));
    console.log("Multiplication result:", multiplication(5, 3));
}

function task2() {
    function greet(name) {
        return "Hello " + name;
    }

    console.log(greet("John"));
}

function task3() {
    function addAndMultiply(x, y, z) {
        let sum = x + y;
        return sum * z;
    }

    console.log("Result of adding and multiplying:", addAndMultiply(2, 3, 4));
}

function task4() {
    function checkEvenOrOdd(number) {
        if (number % 2 === 0) {
            console.log(number + " is even");
        } else {
            console.log(number + " is odd");
        }
    }

    checkEvenOrOdd(5);
}

function task5() {
    function triangleType(side1, side2, side3) {
        if (side1 === side2 && side2 === side3) {
            console.log("Equilateral triangle");
        } else if (side1 === side2 || side1 === side3 || side2 === side3) {
            console.log("Isosceles triangle");
        } else {
            console.log("Scalene triangle");
        }
    }

    triangleType(5, 5, 5);
}
  

function task1() {
    let car = {
        brand: "Toyota",
        model: "Corolla",
        year: 2022,
        color: "Red",
        start: function() {
            console.log("Start");
        },
        break: function() {
            console.log("Break");
        }
    };

    car.start();
    car.break();
}

function task2() {
    let person = {
        firstName: "John",
        lastName: "Doe",
        fullName: function() {
            console.log(this.firstName + " " + this.lastName);
        }
    };

    person.fullName();
}

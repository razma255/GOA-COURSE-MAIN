      // Task 1
      function swapText() {
        var firstText = document.getElementById("first").innerText;
        var secondText = document.getElementById("second").innerText;
        var thirdText = document.getElementById("third").innerText;

        document.getElementById("first").innerText = secondText;
        document.getElementById("second").innerText = thirdText;
        document.getElementById("third").innerText = firstText;
    }

    // Task 2
    var number = 0;
    var numberElement = document.getElementById("number");

    function subtract() {
        number--;
        numberElement.innerText = number;
    }

    function reset() {
        number = 0;
        numberElement.innerText = number;
    }

    function add() {
        number++;
        numberElement.innerText = number;
    }

    // Task 3
    function changeColor(color) {
        var paragraphs = document.getElementsByClassName("paragraph");
        for (var i = 0; i < paragraphs.length; i++) {
            paragraphs[i].style.color = color;
        }
    }

    // Task 4
    var carInfo = {
        brand: "Toyota",
        model: "Camry",
        year: 2022,
        color: "Black",
        engine: "V6",
        getFullInfo: function() {
            return "Brand: " + this.brand + ", Model: " + this.model + ", Year: " + this.year + ", Color: " + this.color + ", Engine: " + this.engine;
        }
    };

    function displayCarInfo() {
        alert(carInfo.getFullInfo());
    }

    // Task 5
    var movie1 = {
        name: "Inception",
        genre: "Science Fiction",
        releaseYear: 2010
    };

    var movie2 = {
        name: "The Dark Knight",
        genre: "Action, Crime, Drama",
        releaseYear: 2008
    };

    var movie3 = {
        name: "Interstellar",
        genre: "Science Fiction",
        releaseYear: 2014
    };

    function displayMovieInfo(movie) {
        alert("Name: " + movie.name + "\nGenre: " + movie.genre + "\nRelease Year: " + movie.releaseYear);
    }

    // Task 6
    function calculate(operation) {
        var num1 = parseFloat(document.getElementById("num1").value);
        var num2 = parseFloat(document.getElementById("num2").value);
        var result;

        switch (operation) {
            case 'add':
                result = num1 + num2;
                break;
            case 'subtract':
                result = num1 - num2;
                break;
            case 'multiply':
                result = num1 * num2;
                break;
            case 'divide':
                result = num1 / num2;
                break;
            case 'equal':
                result = num1 === num2;
                break;
            default:
                result = "Invalid operation";
        }

        alert("Result: " + result);
    }
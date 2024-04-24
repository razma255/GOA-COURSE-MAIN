function Address(name, surname, age, residence, school) {
    this.name = sandro;
    this.surname = razmadze
    this.age = age;
}


Address.prototype.printInfo = function() {
    console.log(`Name: ${this.name}`);
    console.log(`Surname: ${this.surname}`);
    console.log(`Age: ${this.age}`);
    console.log(`Residence: ${this.residence}`);
    console.log(`School: ${this.school}`);
    console.log("-------------------");
}

var familyMember1 = new Address("John", "Doe", 30, "New York", "XYZ School");
var familyMember2 = new Address("Jane", "Doe", 25, "Los Angeles", "ABC School");

familyMember1.printInfo();
familyMember2.printInfo();

familyMember1.age = 35;
familyMember1.residence = "San Francisco";
familyMember2.age = 28;
familyMember2.residence = "Chicago";

familyMember1.printInfo();
familyMember2.printInfo();

var identicalObject = new Address("Alice", "Smith", 30, "New York", "XYZ School");
console.log(familyMember1 == identicalObject); 

function Forecast(location, duration, weather, conditions) {
    this.location = location;
    this.duration = duration;
    this.weather = weather;
    this.conditions = conditions;
}

// Print method for Forecast objects
Forecast.prototype.printForecast = function() {
    console.log(`Location: ${this.location}`);
    console.log(`Duration: ${this.duration}`);
    console.log(`Weather: ${this.weather}`);
    console.log(`Conditions: ${this.conditions}`);
}

var myForecast = new Forecast("New York", "1 week", "Sunny", "Clear skies");

myForecast.printForecast();

/*
Lab 5 Purpose
-------------
This lab helps students practice object-oriented design and clean code principles.
The given code works, but its design has several problems related to SOLID principles.

What students should do
-----------------------
1. Read the code and identify the design problems.
2. Refactor the code while keeping the same overall idea.
3. Apply:
   - Single Responsibility Principle (SRP)
   - Open/Closed Principle (OCP)
   - Dependency Inversion Principle (DIP)
   - Abstraction
   - Inheritance
   - Polymorphism
4. Make the code easier to extend when a new vehicle type or storage type is added.
*/


/*
Required outcome
----------------
- Create a general abstraction for vehicles.
- Replace type-based if/else logic with subclasses.
- Separate storage/saving responsibility from vehicle behavior.
- Make saving depend on an abstraction, not a concrete class.
- Demonstrate the solution using different vehicle types and storage types.
*/
class Storage {
  save(data) {
    console.log('data must be savved')
  }
}
class Database extends Storage {
  save(data) {
    console.log(`Saving data to database: ${JSON.stringify(data)}`);
  }
}
class LocalFile extends Storage {
  save(data) {
    console.log(`Saving data to local file: ${JSON.stringify(data)}`);
  }
}

class Vehicle {
  constructor(type, details) {
    this.type = type;
    this.details = details;
  }
  showDetails() {
    console.log(`Vehicle type: ${this.type}, details: ${JSON.stringify(this.details)}`);
  }
  calculateRentalCost() {
    console.log('implement please ya abny');
}
save(storage)
{  storage.save(this.details);}
}

//-----------------------------------
class Car extends Vehicle {
  constructor(details) {
    super("Car", details);
  }
  showDetails() {
      console.log(
        `Car model: ${this.details.model}, daily rate: ${this.details.dailyRate}`,
      );
  }
  calculateRentalCost() {
    return this.details.dailyRate * this.details.days;
  }
}
//--------------------------------------
class Bike extends Vehicle {
  constructor(details) {
    super("Bike", details);
  }
  showDetails() {
    console.log(
      `Bike model: ${this.details.model}, hourly rate: ${this.details.hourlyRate}`,
    );
  }
  calculateRentalCost() {
    return this.details.hourlyRate * this.details.hours;
  }
}
//--------------------------------------
class Truck extends Vehicle {
  constructor(details) {
    super("Truck", details);
  }

  showDetails() {
    console.log(
      `Truck model: ${this.details.model}, per km rate: ${this.details.ratePerKm}`,
    );
  }
  calculateRentalCost()
  {
   return this.details.ratePerKm * this.details.distance;

  }
} 


// Example usage
// Create:
// - a car rented for 3 days
// - a bike rented for 5 hours
// - a truck rented for 120 km
//
// Save:
// - car to database
// - bike to local file
// - truck to both database and local file

const localFile = new LocalFile();
const database= new Database();
const car =new Car ({ model: "Skodua", dailyRate: 50, days: 3 });
car.showDetails();
console.log('car rent : ' + car.calculateRentalCost() + ' dollars');
car.save(database);

const bike = new Bike({ model: "Rakbny", hourlyRate: 10, hours: 5 });
bike.showDetails();
console.log ('bike rent :'+ bike.calculateRentalCost()+ 'dollars');
bike.save(localFile);

const truck = new Truck({ model: "Ford", ratePerKm: 0.5, distance: 120 });
truck.showDetails();
console.log ('truck rent :'+ truck.calculateRentalCost()+ 'dollars');
truck.save(database);
truck.save(localFile);



from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year, mileage, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available

    @abstractmethod
    def display_details(self):
        pass

    def rent(self):
        if self.available:
            self.available = False
            print(f"The {self.make} {self.model} has been rented.")
        else:
            print("Vehicle is not available for rent.")

    def return_vehicle(self):
        if not self.available:
            self.available = True
            print(f"The {self.make} {self.model} has been returned.")
        else:
            print("Vehicle is already available.")

class Car(Vehicle):
    def __init__(self, make, model, year, mileage, available=True):
        super().__init__(make, model, year, mileage, available)
        self.type = "Car"

    def display_details(self):
        print(f"Type: {self.type}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} km")
        print(f"Availability: {'Available' if self.available else 'Not Available'}")
        print()

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage, available=True):
        super().__init__(make, model, year, mileage, available)
        self.type = "Motorcycle"

    def display_details(self):
        print(f"Type: {self.type}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} km")
        print(f"Availability: {'Available' if self.available else 'Not Available'}")
        print()

# Usage example
car1 = Car("Toyota", "Corolla", 2020, 20000)
car2 = Car("Honda", "Civic", 2018, 30000)
motorcycle1 = Motorcycle("Yamaha", "YZF-R6", 2021, 5000)

car1.display_details()
car2.display_details()
motorcycle1.display_details()

car1.rent()
car1.display_details()
car1.return_vehicle()
car1.display_details()

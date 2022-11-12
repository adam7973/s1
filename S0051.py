"""
Inheritance and polymorphism:

now we want to represent an electric car with the class ElectricVehicle
its attributes and methods are similar to the class Vehicle, but not identical.
we do not have to copy&paste the class code from Vehicle. Instead we define the class ElectricVehicle based on the class Vehicle.
this way ElectricVehicle inherits its attributes and methods from Vehicle

Inspect the following code in detail. Find out what every row of code does.
For example by changing the code a bit and then running/debugging the program.

thereafter go on with the next file in numerical order in the teacher's exercise repository.
"""


class Vehicle:  # this starts the definition of a class

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an object of a class
        self.wheels = wheels  # wheels is called an attribute. A attribute is a variable that belongs to an object of a class.
        self.max_speed = max_speed  # Another attribute.

    def __repr__(self):
        return f"Vehicle: {self.wheels} wheels, {self.max_speed} km/h maximum speed"

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


class ElectricVehicle(Vehicle):  # class ElectricVehicle inherits from class Vehicle

    def __init__(self, wheels, max_speed, battery_capacity):
        super().__init__(wheels, max_speed)  # super() refers to the parent class (Vehicle). That way we can reuse the code of Vehicle.__init__
        self.battery_capacity = battery_capacity

    def __repr__(self):
        return f"ElectricVehicle: {self.wheels} wheels, {self.max_speed} km/h maximum speed, {self.battery_capacity} kW capacity"

    def drive(self):  # this replaces the function drive from the parent class (Vehicle). This is called method overriding.
        print("ssssssssss")


car1 = Vehicle(4, 160)
ecar = ElectricVehicle(8, 100, 90)

print(car1)
car1.drive()
print(ecar)
ecar.drive()  # polymorphism
# we seem to just have called the same function "drive" for objects of different types
# in reality we called Vehicle.drive() and ElectricVehicle.drive()
# this is called polymorphism (= many forms). It makes life a lot easier for programmers
# for example can we now have objects of different types in a list and process them conveniently in a for loop:
print("for loop:")
cars = [car1, ecar]
for car in cars:
    car.drive()

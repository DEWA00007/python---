# Car class
class Car:
    def move(self):
        print("Car is driving.")

# Bike class
class Bike:
    def move(self):
        print("Bike is riding.")

# Plane class
class Plane:
    def move(self):
        print("Plane is flying.")

# Same function works for all objects
def travel(vehicle):
    vehicle.move()

# Create objects
car = Car()
bike = Bike()
plane = Plane()

# Call the same function
travel(car)
travel(bike)
travel(plane)
# global variable
traffic_light = "Green"

# module variable
speed_limit = 60

class Vehicle:
    def start_engine(self):
        message = "Engine started."
        print(message)

class Car(Vehicle):
    def __init__(self, make):
        self.make = make

    def start_engine(self):
        message = "Car engine started."
        print(message)

class Bike(Vehicle):
    def __init__(self, type):
        self.type = type

    def start_engine(self):
        message = "Bike engine started."
        print(message)

# Example usage
car = Car("Toyota")
bike = Bike("Mountain")

car.start_engine()  
bike.start_engine()  

print("Traffic light:", traffic_light)
print("Speed limit:", speed_limit) # polymorphism

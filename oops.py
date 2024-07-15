# global variable
traffic_light = "Green"

# module variable
speed_limit = 60

class Vehicle:
    def start_engine(self):
        m = "Engine started."
        print(m)

class Car(Vehicle):
    def __init__(self, make):
        self.make = make

    def start_engine(self):
        m = "Car engine started."
        print(m)

class Bike(Vehicle):
    def __init__(self, type):
        self.type = type

    def start_engine(self):
        m = "Bike engine started."
        print(m)

# Example usage
car = Car("Toyota")
bike = Bike("Mountain")

car.start_engine()  
bike.start_engine()  

print("Traffic light:", traffic_light)
print("Speed limit:", speed_limit) # polymorphism

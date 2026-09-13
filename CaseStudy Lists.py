class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model 
        self.doors = doors
        self.roof = roof 
    
year = input("Enter Year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors: ")
roofs = input("Enter the type of roof: ")

car = Automobile("car", year, make, model, doors, roofs)
print("Vhicle type:", car)
print("===-----------===")
print("Vehicle type:", car.vehicle_type)
print("Make:", car.year)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("type of roof:", car.roof)

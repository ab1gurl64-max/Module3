from Automobile import Automobile #inheritence 

def main():
    vehicle_type = "car"
    #user inputs
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Doors(2 or 4): ")
    roof = input("Roof(solid or sun roof): ")
    #assigning attributes 
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    #printing attributtes 
    print("Vehicle type: ", car.vehicle_type)
    print("Year: ", car.year)
    print("Make: ", car.make)
    print("Model: ", car.model)
    print("Doors: ", car.doors)
    print("Roof: ", car.roof)
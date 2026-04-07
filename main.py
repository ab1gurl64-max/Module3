from Automobile import Automobile

def main():
    vehicle_type = "car"

    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Doors(2 or 4): ")
    roof = input("Roof(solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("Vehicle type: ", car.vehicle_type)
    print("Year: ", car.year)
    print("Make: ", car.make)
    print("Model: ", car.model)
    print("Doors: ", car.doors)
    print("Roof: ", car.roof)
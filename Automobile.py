from Vehicle import Vehicle #inherit from the vechicle class
#automobile class that contains all attributes for automobile and also inherits vechiles attributes
class Automobile(Vehicle):
    def _init_(self, vehicle_type, year, make, model, doors, roof):
        super()._init_(vehicle_type)
        self.year = year
        self.make = make 
        self.model = model
        self.doors = doors
        self.roof = roof
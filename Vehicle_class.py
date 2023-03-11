class Vehicle:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.engine = None

    def __str__(self):
        return "Year: {}\nMake: {}\nModel: {}\nEngine: {}\n".format(self.year,self.make,self.model,self.engine)
        

class DodgeRam(Vehicle):
    make = "Dodge"
    model = "Ram"
    
    def __init__(self, name, year):
        super().__init__(year, DodgeRam.make, DodgeRam.model)
        self.name = name

    def __str__(self):
        return "Name: {}\n{}".format(self.name,super().__str__())


class Engine:
    def __init__(self, kind = None):
        self.kind = kind


dr = DodgeRam("Bob", 2020)
print(dr) #19, 20, 8, 9

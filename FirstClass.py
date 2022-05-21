# Our first class

class DodgeRam:
    
    
    def __init__(self, color, doors, wheels, model):
        self.color = color
        self.doors = doors
        self.wheels = wheels
        self.model = model
    
    def drive(self):
        return f"Driving a dodge ram and it is the {self} instance\n"
     

d1 = DodgeRam()

print(d1.drive())



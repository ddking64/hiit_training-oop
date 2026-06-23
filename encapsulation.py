class Car:
    def __init__(self, name, color):
        self.__name = name
        self.color = color
    
    
    def getName(self):
        return self.__name
    
car1 = Car("Benz" , "Blue")


car1.__name="gwagon"
print(car1.__name)
print(car1.getName())
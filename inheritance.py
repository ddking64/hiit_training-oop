class Animal:
    def _init_(self, name, no_of_legs) -> None:
        self.name=name
        self.no_of_legs = no_of_legs
        
        
        
#inheritance


class Dog(Animal):
    def nameLeg(self):
        print(f"Name: {self.name},Leg:{self.no_of_Legs}")
        
        
my_dog = Dog(name="Tig",no_of_legs=4)
your_dog = Dog(name="Tom", no_of_legs=5)


print(my_dog.nameLeg())
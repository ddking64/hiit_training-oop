
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def category(self):
        if self.age <= 18:
            category="Underage"
        else:
            category="Adult"
        return category
    
    def displaydetails(self):
        print(f"Full name: {self.name}, age:{self.age}, Category:{self.category()}")
    
    def Age(self):
        print(f"Age: {self.age}")
persons=[]
for i in range (1):
    name = input("Enter your Full-name: ")
    age = int(input("Enter your age: "))
    person = Person(name,age)
    
    # add person to the list
    persons.append(person)

for i in persons:
    print("----------")
    person= persons[i]
    person.displaydetails()
    
for i in range(len(persons)):
    print(f"-----------Person{ i+1}----------")
    person= persons[i]
    person.displaydetails()




    
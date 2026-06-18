class Student:
    def __init__(self, fname, lname, age, year):
        self.fname=fname
        self.lname=lname
        self.age= age
        self.year=year

    def displaydetails(self):
        print(f"Name is: {self.fname} {self.lname}, Age is: {self.age}, Year is: {self.year}")

s1= Student("David", "Ominu", 5, 2026)

print(s1.displaydetails())
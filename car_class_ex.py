class Car: 
    def __init__(self,color, brand , max_speed, year):
        self.color= color
        self.brand = brand
        self.max_speed = max_speed
        self.year=year
    
    def print_color(self):
        print (f"Color: {self.color}")

my_car1=Car("Blue", "Toyota", "180km/h", "2025")       


my_car1.print_color()

class Vehicle:
    running = False
    
    def __init__(self,owner)->None:
        self.owner = owner
        
        
        
    def is_running(self):
        if self.running:
            print(f"{self.owner}'s vehicle car is running")
        else:
            print(f"{self.owner}'s vehicle car is not running")
            
            
car1 = Vehicle("G-wagon")


            
            
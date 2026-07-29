# From today let's start object oriented Programming

# object --> A bundle of realted attributes (variable) and methods  
#             (functions) 
#           Ex -->   phone ,cup , book
#              You need  a class to create many object

# Class ---> A blue-print used to design the structure and layout
#                 of an object



class Car :
    # Attributes:
    def __init__(self, model, year, color,for_sale):   # Constructor method in python ( self is The constructor)
                                                  # of the Class Car.. and other attributes are added by ourself
       self.model = model
       self.year = year
       self.color = color
       self.for_sale = for_sale
  
    def drive(self):     # Methods
        print(f"You drive the {self.color} {self.model}")

    def stop(self):      # Methods
        print(f"You stopped the {self.color} {self.model }") 

    def describe(self):  # Methods
        print(f"{self.year} {self.color} {self.model}")              

car1 = Car("Mustang",1975,"Grey",False) 
car2 = Car("RangeRover",2022,"Black","True") # we can add more car like car3,car4....

print(car1.model)      
print(car1.year)      
print(car1.color)      
print(car1.for_sale)  
car1.drive() 
print()   

print(car2.model)      
print(car2.year)      
print(car2.color)      
print(car2.for_sale)  

car2.stop()

print()
print()

print("Car Descpritions ::::")
print()
car1.describe()
car2.describe()

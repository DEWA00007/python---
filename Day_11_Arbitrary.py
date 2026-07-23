# ARBITRARY 

# *args --> allows you to pass multiple non-key arguments
# **kwargs--> allows you to pass multiple keyword arguments
    #  * unpacking  operators

def add (*args): # We donot need to declare how many argument if we use *args
    total = 0    # *args is not compulsory name--> anything can be name just *name
    for arg in  args:    
      total += arg
    return total
 
print(add(1,2,4,6,7))     # We can pass as much we want .. Result will come

print()
print()

# A function to display the name : 
def name(*args):
   for arg in args:
      print(arg, end=" ")

name("Mr.","Alehandro","Garnacho","(The doing-nothing machine)")
print()
print()


#          **kwargs 

def address(**kwargs):     # **kwargs is a dictionary so we use key,value
   for key,value in kwargs.items():
      print(f"{key} : {value}")

address(Country = "Nepal",
        Province = "Koshi",
        District = "Sunsari",
        City = "Inaruwa",
        House_no ="56 K")
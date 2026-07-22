# Functions:-->  A block of reusable code
#                place () after the function name to invoke it
                # to define a function usee--> def and funciton name

"""def happy_birthday():
    print("Happy birthday to you !")       # defining the function
    print("You are one more year old!") 
    print()

happy_birthday()  # this is used to call the function
happy_birthday()  
happy_birthday()  """


# passing the arguments:  ( we can add many argument in same parameter)
                            # the order must match .. Position of parameters
def greatest_player(name,age):  # while defining function we passes an argument(that can be anything a variable or value etc)   
    print(f"G.O.A.T is : {name}")  
    print(f"The age of the greatest player of football is  : {age}")

greatest_player("Ronaldo",41) # calling function with a value 
                           # for the argument of the function                           
print()

# A function to display the invoice 
def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on our :{due_date}")

display_invoice("Harry",1200,"01/07")
print()
print()


#  Return statement ---> used to end the function
#                        and sent result back 

#simple example to understand : 

def add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z

print(add(1, 5))
print(subtract(2, 3))
print(multiply(4, 5))
print(divide(10, 4))

print()
print()

# A function to create a full name 

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name=(create_name("harry","maguire"))
print(full_name)
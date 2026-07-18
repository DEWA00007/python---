# A while loop repeats as long as its condition is True.
#example : 

name = input("Enter Your name: ")
while name== "":    
    print("You didn't enter your name") 
    name = input("Enter Your name: ") 
print(f"Hello {name} !")  
   
# what happens here is : 
# The loop keeps asking for a name while the input is empty.
# Once the user enters a valid name, the condition becomes False and the loop stops.
# Then the program prints a greeting with the entered name.


# Asking user age :
age = int(input("Enter your age : "))
while age < 18:
    print("Sorry You didnot match the age requirement")
    age = int(input("Enter your age : "))
print("Congrats you meet the age requirement!! ")    



# Examples of while loop  using logical operators

game = input("Enter your favourite game (e to exist): ")
while not game =='e':
    print(f"Your fav game is {game}")
    game = input("Enter another game u like (e to exist)")
print("Thanks for telling me !😊")


#Asking user to enter the no. between 1 and 10
num = int(input("Enter a number between 1 to 10 : "))
while num < 1 or num > 10:
    print("Sorry u didn't match the requirement")
    num = int(input("Enter again a number between 1 to 10 : "))
print(f"Congrats you did it! your numbers was {num} which is between 1 and 10!")

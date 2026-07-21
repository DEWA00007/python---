# A number guessing program

import random

lowest_num = 1
highest_num = 50
answer = random.randint(lowest_num,highest_num)
guesses = 0  # this guesses we will use to know no.of guess it take to find true answer
is_running = True  # True is used to run the while loop

print("Number Guessing Game")
print(f"Select a number between {lowest_num}  and {highest_num}")

while is_running:
    guess = (input("Enter your guess: "))

    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if guess<lowest_num or guess>highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("Too Low! Try again") 
        elif guess>answer:
            print("Too high ! Try again") 
        else:
            print(f"Correct the answer was : {answer}")
            print(f"Number of guesses you take: {guesses}") 
            is_running = False         
    else:
        print("Invalid guess !")
        print(f"Select a number between {lowest_num} and {highest_num}")    
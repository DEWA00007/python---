import random

number = random.randint(1, 100)

print("🎮 Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! 📉")
    elif guess > number:
        print("Too high! 📈")
    else:
        print("🎉 You got it!")
        break
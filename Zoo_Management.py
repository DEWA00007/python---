# A Zoo management Program

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal sound")



class Lion(Animal):
    def sound(self):
        print(self.name, "says Roar!")


class Elephant(Animal):
    def sound(self):
        print(self.name, "trumpets!")


class Monkey(Animal):
    def sound(self):
        print(self.name, "chatters!")


zoo = []

n = int(input("How many animals do you want to add? "))

for i in range(n):
    animal_type = input("\nEnter animal (lion/elephant/monkey): ").lower()

    # Keep asking until a name is entered
    while True:
        name = input("Enter animal name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please enter a name.")

    if animal_type == "lion":
        zoo.append(Lion(name))
    elif animal_type == "elephant":
        zoo.append(Elephant(name))
    elif animal_type == "monkey":
        zoo.append(Monkey(name))
    else:
        print("Invalid animal! Skipping...")

print("\n===== Zoo Animals =====")

for animal in zoo:
    animal.sound()
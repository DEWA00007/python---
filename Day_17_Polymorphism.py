# Polymorphism --> means same name with many forms
 #               Two ways to achieve this ::>
#                1. Inheritance 
#                2."Duck typing"--> object must have necessary attributes/methods


# Parent (Base) class
class Animal:
    def __init__(self, name):
        self.name = name

    # This method is meant to be overridden by child classes
    def speak(self):
        return "Some generic animal sound"

    # This method is inherited by all child classes
    def introduce(self):
        print(f"My name is {self.name}.")


# Child class 1
class Dog(Animal):

    # Overriding the speak() method
    def speak(self):
        return "Woof! Woof!"


# Child class 2
class Cat(Animal):

    # Overriding the speak() method
    def speak(self):
        return "Meow!"


# Child class 3
class Cow(Animal):

    # Overriding the speak() method
    def speak(self):
        return "Moo!"


# Polymorphic Function

# This function accepts an Animal object.
# It doesn't care whether it's Dog, Cat, or Cow.
# It simply calls the speak() method.
def animal_sound(animal):
    animal.introduce()                 # Inherited method
    print("Sound:", animal.speak())    # Overridden method
    print("-" * 30)



# Creating Objects

dog = Dog("Buddy")
cat = Cat("Kitty")
cow = Cow("Bella")


# Individual Calls

print("Individual Calls")
print()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)



# Polymorphism with a List

print("\nUsing a List")
print()

animals = [dog, cat, cow]

# The loop doesn't know which specific class
# each object belongs to.
# It simply calls speak() on every object.
for animal in animals:
    print(f"{animal.name} says {animal.speak()}")



# isinstance() Demonstration

print("\nChecking Inheritance")
print()

print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True
print(isinstance(cat, Animal))   # True
print(isinstance(cow, Animal))   # True



# Parent Class Reference

print()

# Although the variable is conceptually treated
# as an Animal, it actually refers to a Dog object.
animal = Dog("Rocky")

# Python calls Dog's version of speak(),
# not Animal's version.
print(animal.speak())



# What if a child doesn't override speak()?

class Lion(Animal):
    pass


lion = Lion("King")

print("\nChild Without Overriding")
print()

# Since Lion doesn't define speak(),
# it inherits the parent's implementation.
print(lion.speak())
                                       
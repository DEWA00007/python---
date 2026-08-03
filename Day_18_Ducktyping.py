# Dog class
class Dog:
    def speak(self):
        print("Woof!")

# Cat class
class Cat:
    def speak(self):
        print("Meow!")

# This function doesn't care if it is a Dog or a Cat.
# It only expects the object to have a speak() method.
def make_sound(animal):
    animal.speak()

# Create objects
dog = Dog()
cat = Cat()

# Pass both objects to the same function
make_sound(dog)   # Output: Woof!
make_sound(cat)   # Output: Meow!
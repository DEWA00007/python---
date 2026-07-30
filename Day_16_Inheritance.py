# Inheritance --> Allows a class to inherit attributes and methods from another class
#                  Helps in code resusablity and extensibility
#                  class Child(Parent)


class Animal:
    def __init__(self,name):
      self.name = name
      self.is_alive = True

    def eat(self):
       print(f"{self.name} is eating")

    def sleep(self):
       print(f"{self.name} is sleeping") 

class Dog(Animal):
   def speak(self):
      print("WOFF WoFF!!")

class Cat(Animal):
  def speak(self):
        print("Meoww meoww")

class Mouse(Animal):
   def walk(self):
      print("chuk chuk chuk chuk.....")
   
dog = Dog("Tommy")
cat = Cat("Billa")
mouse = Mouse("Musa")

print(f"The name of the dog is: {dog.name}")
print(f"Is it still alive ? :{dog.is_alive}")
dog.speak()
dog.eat()
dog.sleep()

print()
print()

print(f"The name of the cat is: {cat.name}")
print(f"Is it still alive ? :{cat.is_alive}")
cat.speak()
cat.eat()
cat.sleep()

print()
print()

print(f"The name of the Mouse is: {mouse.name}")
print(f"Is it still alive ? :{mouse.is_alive}")
mouse.walk()
mouse.eat()
mouse.sleep()

         
        
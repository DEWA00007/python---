# Multiple Inheritance--> inherit from more than one parent class
#                          C(A, B)

class Animal:
    def eat(self):
        print("This animal is eating")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")
        

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass 
       

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

print()
rabbit.eat()
fish.eat()
hawk.eat()
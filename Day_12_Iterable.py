# Iterables = An object/collection that can return its element
#             one at a time, allowing it to be iterated over a loop
 
num = [1,2,3,4,5]   #  List are iterable
for element in reversed(num):
    print(element,end=" ")
print()
print()

# Tuple is also iterable
fruits=("apple","banana","orange","mango","Star-fruit")
for item in fruits:
    print(item)
print()    
print()

# Sets : --> Not reversable .. 

cars={"Mercedes","Range-Rover","Audi","Lamborghini"}
for car in cars:
    print(car)
print()
print()


# Strings:
# create a string \

name="Antony Martial"
for character in name:
    print(character,end="")
print()
print()

# Dictionaries are also iterables

my_dictionary ={"A": 1, "B" : 2, "C" : 3, "D" : 4}
for key,value in my_dictionary.items():
    print(f"{key}-{value}")    
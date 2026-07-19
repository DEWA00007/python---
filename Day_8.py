# collection = single " variable" use to store multiple values

# List = [] ordered and changable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK . No duplicate
# Tuple = () ordered and unchangable. Duplicates Ok . FASTER


#List[] --> ordered, changeable

"""fruits = ["apple","banana","grapes","mango"]  # Any of the collection method can be used 
                                              # This helps to store different value in same variable
print(fruits) 
print()  # for space
print(fruits[2])  # Prints the value of fruits of 'n' index                                         
print()
print(fruits[0:3]) # Prints from 0 index to 2 indexes all values(as end is always exclusive )
print()
print(fruits[::2]) # for every second element
print()
print(fruits[::-1]) # (:: for steps) . -1 for backwaards.. 
print()


# Using loop to print that fruits:
for f in fruits:
    print(f)

print()
    # changing the value ; 
fruits[0]="Orange"
print(fruits[0])
print()


fruits.append("pineapple")  # .append is used for adding another element in list
print(fruits)
print()

#To remove  any element
fruits.remove("Orange")
print(fruits)
"""

# Set{ } unorederd, immutable  but we can add or remove (no duplicates)

"""players={"Ronaldo", "Messi", "Neymar","Mbappe"}  # Every time the order changes while printing
print(players)
print()
print("lamine" in players)  # this check the give name " " is in the set{ }or not(boolean)

# We cannot use the indexing [n] in the set !!
# We can't change the value of set but can add and remove 
print()
players.add("Lewondoski")
print(players)
print()

players.remove("Mbappe")
print(players)
print()

players.pop()  # this will remove whatever the first element is and in set it will be random every time
print(players)
print()

players.clear()  # To clear the whole set
print(players)"""


# Tuples()--> fast . ordered. unchangable

colors = ("red","green","purple","blue")
print(colors)
print()

print(len(colors))  # help to find the length of the element(here --4 rgpb)

print()

print("green"in colors) # Boolean true or false 
print()

# here in tuple the index can be found
print(colors.index("purple"))
print()

# We can count any given elements 
print(colors.count("green"))  # Only 1 green is in the tuple
print()

for c in colors:
    print(c)

import random   # Used to generate random int,variable etc

"""num=random.randint(1,6)  # Used to generate random integer (1,6)--> it is range
print(num)"""

# Another method by declaring variable

low = 1
high = 100
print(random.randint(low,high))  # randomly generates the number 
                                 # between 1 and 100 and num changes
                                 # every time
print()

print(random.random()) # this randomly generates floating point number
                        # between 0 and 1

# for random character(strings or values)
# let's generate simple rock paper scissors

options =("rock","paper","scissors")
my_choice = random.choice(options)
print(f"I choose : {my_choice}")      # it also changes every time



# Another method (shuffle):: 
# let's take card example

cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)   # not declaring variable in this !!
print(cards)  # cards are shuffled everytime
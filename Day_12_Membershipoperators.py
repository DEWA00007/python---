# Membership Operators --> used to test whether a value or variable is 
#                           found in a sequence(string,list,tuple,set or dictionary)
#                 1. in   --> boolean return true or false used to test if value or variable is found in a sequence
#                 2. not in 

# example ---> in

word="apple"
letter = input("Guess a letter in secret word: ")
if letter in word:
    print(f"There is  {letter} ")
else:
    print(f"{letter} was not found")    

# for "not in"---> 
# if letter not in word:
#   print(f"{letter} was not found )
# else:
#  print(f"{letter } was found)    



print()
print()

# Let's try a set::

students = {"Harry","Ben","Wiliam","Gaberial"}
student=input("Enter the name of Student: ")
 
if student in students:                 # We can also use not in
    print(f"{student} is a Student")
else:
    print(f"{student} was not found")    
print()
print()


# Now let's try dictionary

grades={"Saka":"A+",
        "Rice":"A",
        "Victor":"A-",
        "Raya":"B+"}
student=input("Enter the name of student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}") 
else:
    print(f"{student} was not found")    

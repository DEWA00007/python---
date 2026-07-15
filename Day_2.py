# String and it;s some methods.. 
name = input(" Lionel Messi or  Cristiano Ronaldo ? ")

# to Remove white space from str..
name = name.strip()    
print(name)

#Capatialize the text..
name = name.title() # this make the first letter capital of whole name
print(name)

# We can combine various str attributed together.. lik3
# name = name.strip().title().capitialize()


# Split user name to first name and last name 
first, last = name.split(" ")
print("Hello ", first)
print (last)


#Data typess::: 


# """"  and """" is also comment(multi-line)!!
""" Next Data type---> integer( int ) 
x = int(input("Enter x ;"))
print(x)"""


# float

# x = float(input("Enter x : "))

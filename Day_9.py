# 2D list.. ---> List made up of a list

"""fruits=    ["apple","banana","orange","grapes"]
vegetables=["potatoes","carrots","cabbages"]
meats=     ["chicken","fish","muton"]

groceries = [fruits,vegetables,meats]  # This a 2D list.

print(groceries)  # Prints all list items of groceries elements
print()
 
print(groceries[0]) # This prints the 0 index of groceries(here is fruits)
print()                    # All element of fruits will be printed


print(groceries[0][2]) # This means : It will print the value
                        # of [0] means '0' index row which is
                        # fruits here(1st row), and 2 index means 
                        # the value of that same row which is 'orange'
                        # will be printed..
                        """


# Creating a 2 Dimensional keypad of phone    
# I am using tuple 

num_pad =((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()    
name = input("Enter your name : ")

#I am taking example of (name) variable

# len(name) --> find the lenght (Count space as well)
# name.find(" ") -->find the first occurance of space : eg: Car air---> (3) after r
# we can also find any digits eg: name= Car air and name.find("a")-->1
# The name.find("a") only shows the first occurance ..
# for last occurance another method is there : name.rfind("a")
# name.rfind("a") --> 4 

# To capitalize :: name.capitalize()  -->only capitalize the first letter
#For making uppercase letter :: name.upper()
#For lower case :: name.lower()

#To check if string contains only digit: (Should contain only digit no combined ..)
# name.isdigit()  -->Gives boolean answer only.

#To check the string contains only alphabets (If it contains even sapce the result is False)
# name.isalpha()--->Same gives boolean only (only letters no space no digit)

# To count any thing repeated 
# .count() 

# Replace method to replace any occurance of one character with another
# .replace("", "")
#example: a phone.no = 123-456-789-01 then we can replace the dashes(-) with space or anyother thing 
# phone_no.replace("-"," ")---> it replaces - with space 

# for a list of all this comprehensive methods we have 
#print(help(str))
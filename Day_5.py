 # conditional

#  Write a program to for voting eligibility..
age=int(input("Enter your age: "))

if age>=110:
    print("You might have mistaken the age")

elif age>=18:
    print("You are eligible to cast vote")

else:
    print("You are still child !! ")    




#Find the largest number  among three numbers:: 
a = int(input("Enter A :"))   
b = int(input("Enter B :"))   
c = int(input("Enter C :"))   

if a>=b and a>=c :
    print("A is largest")

elif  b>=c:
    print("B is largest")

elif a==b==c :
    print("All numbers are equal")

else :
    print("C is largest")    




# Asking user if they want some food ?
response = input("Are you hungry ? (Y/N): ")

if response =='Y'or response == 'y':
    print("Have some food!!")    
else:
    print("Not hungry than sleep!!")    
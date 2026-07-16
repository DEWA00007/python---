"""#(for boolean condtions:: )
online = False
if online:
    print("User is Online")
else: 
    print("User is offline")   """ 





# A calculator using if else::

operator=input("Choose the operator u want(+ - * /)")
a= float(input("Enter a : "))
b= float(input("Enter b : "))
if operator =='+':
    print(f"The sum of a and b is :{a+b}")
elif operator =='-':
    print(f"The difference between and b is :{a-b} ")
elif operator =='*':
    print(f"The multiplication of a and b is : {a*b}")
elif operator =='/':
    print(f"The division : {round(a/b,2)}")
else:
    print(f"{operator} is not valid!! ")        

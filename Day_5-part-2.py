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



# Python weight converter (k to p and p to k)

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pound (K or P )")
if unit == 'K':
    weight =weight*2.205
    unit ='lbs.'
elif unit == 'P':
    weight /= 2.205
    unit ='kg.'
else :
    print(f"{unit} is not valid")    
print(f"Your weight is : {round(weight, 2)}{unit}")    
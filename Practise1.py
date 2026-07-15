"""#Calculate the area of rectangle 

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
Area = length*width
print(f"Area of rectangle:{Area}cm²")"""


# Shopping Cart Program

item = input("What you want to buy ? ")
price = float(input("What is the price :"))
quantity = int(input("How many do you want ? "))
total = price*quantity
print(f"Your total bill is :${total}")



# find the circumference of circle  and area: 
 
import math

radius = int(input("Enter the radius : "))
Circumference = 2 * math.pi* radius
print(f"The Circumference of the circle is:{round(Circumference,3)}")  # round (,3) ley chai paxadi ko 3 digit matra linxa 

area = math.pi * radius * radius
print(f"Area of the circle is {round(area,2)}cm²")


#find the hypotenous of a right angle triangle
import math

a= float(input("Enter side A: "))
b= float(input("Enter side B:  "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Hypotenous of triangle (H) is : {round(c,2)}")
#Logical Operators:: ( or , and , not ) 
# or ---> at least one condition to be
# and---> both condition must be true
# not---> inverts the condition(True to false , false to true)


"""An outdoor event example ( for Or ..)

temp = 25
is_raining = True
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceld ")
else:
    print("The outdoor event is still scheduled")    
"""



# For 'and' + 'not' :: 
temp =int(input("Enter the temp in °C : "))
is_Sunny = False 

if temp > 30 and is_Sunny:
    print("It is hot outside 🥵") 
    print("It is SUNNY ☀️") 
elif 0<temp<20 and  is_Sunny:
    print("It is a fantastic weather 🙃")   
    print("Neither  hot nor too cold 👌") 
elif temp<0 and is_Sunny:
    print("It is very cold 🥶")

elif temp > 30 and not is_Sunny:
    print("It is hot outside 🥵") 
    print("It is CLOUDY ☁️") 
elif 0<temp<20 and not is_Sunny:
    print("It is a fantastic weather 🙃")   
    print(" CLOUDY☁️") 
elif temp<0 and not is_Sunny:
    print("It is very cold 🥶")
    print("It is very CLOUDY ☁️")
else:
    print("Sometimes may be good sometimes may be bad.. Now ")
    print("Sorry man it's raining ⛈️") 




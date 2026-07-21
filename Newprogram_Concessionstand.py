# Like a mini shop in the theater or anyplace : 
menu={"pizza":3.4,
      "momo": 2.4,
       "ice-cream":5,
       "coke":2.7,
       "chips":4.23}
cart=[]
total=0
print("--------MENU--------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("-------------------------")   
print()
while True:
    food=input("Enter the food items(q to quit): ").lower()
    if food =="q":
        break
    elif menu.get(food) is not None:  # THis will add only the food items from our menu..in cart
          cart.append(food) 
print()                                     # if food is not menu it will not cound/add it
print("-----------YOU SELECTED-----------")     
for food in cart:
     total +=menu.get(food)  # this will show total food items selected in cart
     print(food,end=" ") 
print()
print()
print("---------TOTAL BILL----------")     
print(f"Your total is:  ${total:.2f}")
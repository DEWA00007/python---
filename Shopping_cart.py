# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input("Enter the price of that food :$ "))
        foods.append(food)  # Adds the foods that we enter to a collection
        prices.append(price)  

print("----YOUR CART----")

for food in foods:
    print(food,end=" ")
print()

for price in prices:
    total += price

print(f"Your Total bill is : {total:.2f}$")  # For showing only 2 decimal point

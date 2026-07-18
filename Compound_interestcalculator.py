#Compound Interest Calculator : 

p = float(input("Enter your principal: "))
r = float(input("Enter the rate (%): "))
t = int(input("Enter time (in years): "))

while p <= 0:
    print("Principal must be greater than 0.")
    p = float(input("Enter your principal: "))

while r <= 0:
    print("Rate must be greater than 0.")
    r = float(input("Enter the rate (%): "))

while t <= 0:
    print("Time must be greater than 0.")
    t = int(input("Enter time (in years): "))

si = (p * t * r) / 100
print(f"Simple Interest = {si:.2f}")  # Only takes 2 decimal point 

amount = p * ((100 + r) / 100) ** t
ci = amount - p

print(f"Amount = {amount:.2f}")
print(f"Compound Interest = {ci:.2f}")
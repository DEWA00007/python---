from datetime import date

birth_year = int(input("What year were you born? "))

current_year = date.today().year
age = current_year - birth_year

print("You are", age, "years old!") 
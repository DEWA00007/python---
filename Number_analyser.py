# Number_analyser

numbers = []

print("Number Analyzer")
print("----------------")

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("\nResults:")
print("Numbers:", numbers)
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
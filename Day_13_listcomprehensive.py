# List Comprehension = A concise way to create lists in python
#                      easier and compact than traditional loops
#       formula--->    [expression for value in iterable if condition]


# Creating a list and doubling the number 1 through 10

double=[ x*2 for x in range(1,11)]  # this is easy way and short way than using loops
print(double)
print()
print()



# Let's work with strings::
fruits = ["apple","banana","orange","mango"]
fruits=[ fruit.upper() for fruit in fruits]
print(fruits)
print()
print()



# Now let's work with the if condtion as well:>

numbers=[1, -2, 3, -5, 4, -6]
postive_nums=[num for num in numbers if num>=0]
negative_nums=[num for num in numbers if num<0]
even_nums=[num for num in numbers if num %2 == 0]
odd_nums=[num for num in numbers if num %2 == 1]

print(postive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

print()
print()




# Create a list of grades:> ( passing grades)
grades=[49,60,80,92,30,20]
passing_grades=[ grade for grade in grades if grade>=60]
print(passing_grades)

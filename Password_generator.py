import random

length=int(input("Enter the lenght of password you want: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
             # here we added one random string to choose pass from

password= ""   # Created an empty string to store the password
for i in range(length):  
    password += random.choice(characters)
print(password)

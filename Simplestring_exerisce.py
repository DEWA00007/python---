# validate user input exercise
  # 1. username must not contains more than 12 characters
  # 2. username must not contain space
  # 3. username must not contain digits 

user_name = input("Enter your username: ")



if len(user_name) > 12:
    print("Your username can't be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Your username cannot contains space")
elif not user_name.isalpha():
    print("Your username cannot contains digits")    
else:
    print(f"Welcome {user_name}") 


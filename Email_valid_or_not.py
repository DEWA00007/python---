# A  program to check whether the email is valid or not

email = "harry_maguire@gmail.com"

if "@" in email and "." in email:
    print(f"{email} is a valid email account!")
else:
    print(f"{email} is not a valid account")    
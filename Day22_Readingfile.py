# Python reading files 

import json # for json file

file_path = "output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print(f"File named {file_path} was not found ! ") 

# We have another error type (PermissionError) 

except PermissionError:
    print("Access Denied!!")


# Now to read json file 
    
file_path2 = "C:/Users/dewas/OneDrive/Desktop/output.json"
try:
    with open(file_path2, "r") as file:
        content2 = json.load(file)
        print(content2)

except FileNotFoundError:
    print(f"File named {file_path2} was not found ! ")
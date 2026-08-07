# Python writing Files(.txt, .json, .csv)
"""
txt_data = "I like apple! "
file_path = "output.txt"   # relative path , we can also use the absoulte file path
with open(file_path, "w") as file:
   file.write(txt_data)
   print("Text file was created")



 # Like "w" we have others too 
 # "x" --> This write (create) a file if that is not existed Already
 # "a" --> To append the file and add more output there"""


# For .json file we need to import it

import json
# Let's try a dictionary

employee = {"name": "Harry",
            "age":34,
            "Address":"Manchester"}

File_path = "C:/Users/dewas/OneDrive/Desktop/output.json"

try:
    with open(File_path,"w") as file:
        json.dump(employee, file,indent=4) # dump() will convert dictionary to json string
        print("Json File was created")
except FileExistsError:
    print("File already exists!")        
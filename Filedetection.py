# Python file detection

import os

file_path = "test.txt"   # relative method if file is in the same folder than

if os.path.exists(file_path):    # This gives us boolean vlaue of it file exist or not
   print(f"The location '{file_path}' exists")

   
   if os.path.isfile(file_path):
      print("That is a file")

   elif os.path.isdir(file_path):
      print("THis is a folder")  

else:
   print("That location doesn't exists")   
print()

# If file is in different folder : 

file2_path = "E:/New folder"  # Like this for a file outside a folder

if os.path.exists(file2_path):    # This gives us boolean vlaue of it file exist or not
   print(f"The location '{file2_path}' exists")

   if os.path.isfile(file2_path):
      print("That is a file")

   elif os.path.isdir(file2_path):
      print("THis is a folder")  


else:
   print("That location doesn't exists")   
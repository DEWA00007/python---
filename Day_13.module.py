# module = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program resuable seperaate files

# print(help("modules"))

# import math
# import math as m


# now we will import some module that I will create in another file named
 # example_mod.py

import example_mod

result1 = example_mod.pi
result2= example_mod.square(2)
result3= example_mod.cube(4)
result4= example_mod.circumference(3)
result5= example_mod.area(5)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
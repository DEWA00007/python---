# printing the pattern : 
"""
   *
   * * 
   * * *
   * * * *
   * * * * *
"""
for i in range(1,6):
    for x in range(i):
        print("*",end="")
    print()    

print()
print()


# printing backward traingle: 
for i in reversed(range(1,6)):
    for x in (range(i)):
        print("*", end="")
    print()   
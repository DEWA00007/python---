# for loops = executes a loop block of code a fixed number of times.
#             You can iterate over a range, string, sequence etc.


"""# Basic counting to 10 .. (1, 11)-->11 is exclusive here.
for i in range(1, 11):
    print(i)    
print("1-10 was counted!! ")

# To count backwards: 
for x in reversed(range(1,11)) :
    print(x)
print("Happy new Year! ")    

# To count by an 'n' number : 
for i in range(1,11,2):  # here number will be counted on gap of 2
    print(i)"""


# Continue and break ;

for x in range(1,15):
    if x == 11:
        continue    # This is used to skip the iteration(here 11 will be skipped)
    else: 
        print(x)


for i in range(1,8):
    if i == 4:
        break  # break is used to exist (discard) the iteration 
    else:       # ( here after it reaches 4 the iteration(1,2,3)and closed)
        print(i)
   
# Create a count up timer program

import time

def count(end,start = 0): # default value must be after non defalut value !!
    for i in range(start,end+1): # end + 1 because it is exclusive at last         
        print(i)
        time.sleep(1)
    print("That's it !!") 

 # count(15)      

count(30,20) 
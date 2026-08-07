# Working with Date and time in Python ::

import datetime    # Import datetime from our computer/laptop
 
date = datetime.date(2024,7,7) # A random date manuallay wirting
today = datetime.date.today()  # Getting today(Actual realtime) Date
print(date)
print(today)

time =datetime.time(12,30,0) # Random time first hr, min and sec
now = datetime.datetime.now() # 1st datetime is import module 2nd one is a class always needed !     
now = now.strftime("%H:%M:%S ---> %m/%d/%Y")
print(time)
print(now)


target_datetime = datetime.datetime(2030, 1, 1, 8, 19, 17)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target Date has not passed")    

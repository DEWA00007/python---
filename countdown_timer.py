# Countdown timer program
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):  # Start from my_time, count backwards by 1, stop before 0 (0 is not included).
    seconds = x % 60             # Gets the remaining seconds after complete minutes. Example: 125 % 60 = 5
    minutes = int(x / 60) % 60   # Converts seconds to minutes, then % 60 keeps minutes between 0 and 59.
    hours = int(x / 3600)        # Converts total seconds into complete hours. (3600 seconds = 1 hour)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")  # :02 always displays 2 digits. Example: 5 -> 05
    time.sleep(1)                # Wait 1 second before showing the next countdown value.

print("Time's Up")
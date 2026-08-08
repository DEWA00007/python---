# multithreading --> used to perform multiple task concurrently (multitasking)
#                Good for I/O bound task like reading file or fetching data from APIs
#           module--> threading. consytructor -->Thread(target = my_function)                

import threading
import time

def walk_dog(first_name,l_name):
    time.sleep(8)   # It will wait 8 sec and then print the following
    print(f"You finish walking {first_name} {l_name}")

def get_mail():
    time.sleep(4)
    print("You collected the mail")

def trash():
    time.sleep(2)
    print("You take out the trash")

"""# single thread (one-one)
walk_dog()
get_mail()
trash()"""

# Multithreading ( multiple task at given time)
thread1= threading.Thread(target=walk_dog, args=("Tommy","Choi choi")) # This is for thaking the argument and if only 1 argument taken than at last a ',' is neccessary for tupple
thread1.start()

thread2= threading.Thread(target=get_mail)
thread2.start()

thread3= threading.Thread(target=trash)
thread3.start()

thread1.join()     # this join() method works in the way that
thread2.join()      #  At first the threads are complete then 
thread3.join()      # only it prints the printing statement

print("All threads are complete !")
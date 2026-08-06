# exception --> An event that interrupt the flow of the program
#              (ZeroDivisionError, TypeError, ValueError)
#               1.try, 2.except, 3.finally

try:
    num = int(input("Enter a number : "))
    print(1/num)

except ZeroDivisionError :
    print("You cann't divide by zero IDIOT!!!!!")    

except  ValueError :
    print("Only Entering the Numberr ! ") 

except Exception :
    print("Something went wrong") 

finally: # It always executes
    print("Do some cleanup here")        
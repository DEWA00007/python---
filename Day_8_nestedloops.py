# nested loops= A loop within another loops
 
"""for i in range(3): # this is outer loop ( it runs upto 3 times). counter mustn't be same
  for x in range(1,10):              # upper counter diff inner diff ( i and x)
    print(x,end="") # this prints the numbers in same line (what we give " " here.)
  print()     # this is outside inner loop and inside outer loop
              # this help to print 3 times differently on differnt lines
              # eg : 123456789
              #      123456789
              #      123456789 """


# Create a rectangle using symbol :

rows = int(input("Enter the numbers of rows: "))
columns = int(input("Enter the numbers of columns: "))
symbol = input("Enter the symbol you want to use: ")

for i in range(rows):
    for x in range(columns):
        print(symbol,end="")
    print()    
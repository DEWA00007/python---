#Format specifiers ={value:flags} format a value based on what
#                                       flags are inserted

# .(number)f = round to that many decimal places (fixed points)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place a sign to left most position
# : = insert a  space before positive number
# :, = comma seperator


price1 = 3.14159 
price2 =- 987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}")  # This :.2f is used for taking n decimal point 
print(f"Price 2 is ${price2:10}")  #:n (This creates space {here :10 --> 10 spaces after $sign})
print(f"Price 3 is ${price3:02}") # this is used for zero padded 

# like this other format specifier also works 

# We can also use 2 or more specifier at a time..
#Ex;
price4 = 3000.7878545
print(f"Price 4 is {price4 :+,.2f}")
   # + is used to add plus sign in positive number 
   # , is used to seperate the thousand

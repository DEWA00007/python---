# Default argument-->  defalut value for certain parameters
#                      1. Positional  2.DEFAULT  3.keyword  4.arbitrary
# poitional already done ... in Day_11functions

# default arguments

def net_price(Marked_price,discount=0.3,tax=0.04): # for default we assign an value directly at parameters
    return Marked_price*(1-discount)*(1+tax)

#  print(net_price(700,0.2,0.013))  --> this is normal one 

print(net_price(600)) # we only passes the m_p here. cz discount and tax is already 
                      # given on the parameter of the function
print()
print()

# We can also add the discount and tax if it's given already on parameter
 # Answer will be calculated on the new value given while calling function

print(net_price(900,0.07,0.2)) 
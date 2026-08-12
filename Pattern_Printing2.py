# Some other pattern printing
 # inverted pyramid
n = 7
for i in range(1,n+1):
    print(" "*(i-1)+"-"*(2*(n-i)+1))
print()

# Diamond   :

n=7
for i in range(1,n+1):
    print(" "*(n-i)+"^"*(2*i-1)) 

for j in range(1,n+1):
    print(" "*(j-1)+"^"*(2*(n-j)+1))
  
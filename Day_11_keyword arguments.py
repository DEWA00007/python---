# keyword argument --> an argument preceded by an identifier
#                       order of argument doesn't matter

def hello(greeting,title,f_name,l_name):
    print(f"{greeting} , {title} {f_name} {l_name}")

hello("Hello",f_name="Cristiano",title="G.O.A.T",l_name="Ronaldo")
 # here the order will not matter as we give the keyword and it's value
  # other wise the order does matter .. 
  # Imp--> the positional argument must be at first then only the keyword argument


print()
print()

# A program(function) to generate a phone number:(keyword argument)

def ph_num (country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

get_num=(ph_num(country=250,first=60,area=5,last=380)) # order doesn't matter here
print(get_num)


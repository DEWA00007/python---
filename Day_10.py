# Dictionary =  a collection of {key:value} pairs ordered and changables. 
                  #No duplicates

capitals={"Nepal": "Kathmandu",  # this is the way of writing dictionary
          "India":"New Delhi",
          "China":"Beijing"}
 # print(dir(capitals)) ---> To see the different attributes and methods
 #print(help(capitals)) --> Indepth description of the attributes and methods

print(capitals.get("Nepal"))  # .get is used to get any value of dictionary
 

if capitals.get("China"):         # If we use 'japan' for ex.
    print("That capital exist")   # that is not on our dictionary
                                  # it will print else statement
                                  #If it is in our dict. then if condtion
else:
    print("That capital doesn't exist")    


# TO Update the dictinoary : we have .update({"":""}) we can add new + update current
capitals.update({"Portugal":"Lisbon"})    
print(capitals.get("Portugal"))

capitals.update({"India":"Mumbai"})
print(capitals.get("India"))  # here the india capital is updated to mumbai from delhi

# To remove  a key pair value: .pop("")
capitals.pop("China")
print(capitals )


#capitals.clear()  --> to clear the dicitionary
print()


# TO get the keys within the dictionary but not the values, there is a keys method  

print(capitals.keys()) 

print()

for key in capitals.keys():  # for loop is used to iterate over every key
    print(key)


# TO get all of the values within the dictionary-->.values()
print()
print(capitals.values())
print()

for value in capitals.values():
    print(value)
print()

# Items method ---> items = [(),(),()]  -- 2D list of tuple
# items returns a dictionary objects

print(capitals.items())
print()

for  key, value in capitals.items():
    print(f"{key}:{value}")
    # this is used to show all the value and keys together 
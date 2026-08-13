def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters


# Taking input from the user
inches = float(input("Enter length in inches: "))

# Calling the function
centimeters = inches_to_centimeters(inches)

# Displaying the result
print("Length in centimeters:", centimeters)
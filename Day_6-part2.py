# indexing = accessing elements of a  sequence using [](indexing operator)
# [start : end : step] 

credit_number = "1234-5678-9012-3456"
print(credit_number[0])  # It will print the no. from the given index.. 
print(credit_number[0:4]) #It will print first 4 no. from 0 to 4 index..
print(credit_number[:3]) # No need to add first index if using : for print upto some index
print(credit_number[5:9]) # For number in between ..Like 5 index has value 5 and index 9 has value 8
print(credit_number[5:]) # For printing upto the last index no need to add the index just leaving blank also works upto last
print(credit_number[-1]) # Prints from last number. In this case [-1] prints 6
print(credit_number[::3])  # This prints every 'n' numbers.. eg;[::3]-->146-136


#Create a program to get the last 4 digits of a credit card (same credit_number as above)

last_digit = credit_number[-4:]  # -4 means backwarding index 4 from last...-1:6, -2:5..-4:3
print(f"XXXX-XXXX-XXXX-{last_digit}")


# To reverse any thing:: 
# variable = variable[::-1]  # This just start the numbers from the 
                             # last to first as no anypoint of starting index is
                             # given ... So from -1 means from last to  the starting 
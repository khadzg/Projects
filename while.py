# This programme is to calculate the average of user inputs as long as the input is not -1. Once -1 is hit the programme should break.

# Initialise the variables
count = 0
updated_input = 0 

# Ask the user for an input
user_input = int(input("Please input any number: "))

# While the user's input is not -1, ask the user for further inputs
while user_input != -1:
    updated_input += user_input
    count += 1 
    user_input = int(input("Please input any number: "))
    average = (updated_input / (count))

print (f"The average of all numbers that are not -1 is {average}")


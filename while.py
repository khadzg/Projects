# This programme is to calculate the average of user inputs as long as the input is not -1. Once -1 is hit the programme should break.

# define the function
def average_numbers():
    count = 0
    updated_input = 0 
    user_input = int(input("Please input any number: "))
    while user_input != -1:
        updated_input += user_input
        count += 1 
        user_input = int(input("Please input any number: "))
        average = (updated_input / (count))
    print (f"The average of all numbers that are not -1 is {average}")


#run the function
average_numbers()


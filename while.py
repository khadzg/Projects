# This programme is to calculate the average and maximum of user inputs as long as the input is not -1. Once -1 is hit the programme should break.

user_input = int(input("Please input any number: "))

# define the function
def statistics(user_input):
    count = 0
    updated_input = 0 
    numbers_list = []
    while user_input != -1:
        #inputs for average
        updated_input += user_input
        count += 1 
        user_input = int(input("Please input any number: "))
        average = (updated_input / (count))

        #inputs for max
        numbers_list.append (user_input)
        maximum = max(numbers_list)
      
    print (f"The average of all numbers that are not -1 is {average}")
    print (f"The maximum of all numbers that are not -1 is {maximum}")


        
#run the functions
statistics(user_input)

# Libraries
import math

# Functions
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to

# Number checker for floats and ints!!!
def num_check(question, num_type):

    # More detailed value error message
    if num_type == int:
        val_error = "This must be an integer! (a number without a decemal point)"

    elif num_type == float:
        val_error = "This must be a number!"

    else:   # If I mess up the num_type variable again
        print("The program as experienced an error!")
        print("The num_type variable is not an int or float")
        exit() # Quit the program to prevent a crash
            
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <=  0:
                print("This must be a number more than 0")

            else:
                return response
            
        except ValueError:
            print(val_error)

# Main
how_many = num_check("How many items? ", int)
total =num_check("Total costs? $", float)
profit_goal = num_check("Profit goal? ", float)
round_to = num_check("Round to the nearest...? ", int)

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recomended Price: ${:.2f}".format(recommended_price))
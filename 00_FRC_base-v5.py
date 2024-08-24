# Libraries
import pandas
import math

# Functions

# Number checker for floats AND ints!!!
def num_check(question, num_type):

    # More detailed value error message
    if num_type == int:
        val_error = "This must be an integer! (a whole number)"

    else: # If num_type is float
        val_error = "This must be a number!"

            
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

# Yes no checker
def yes_no(question):

    valid_response = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower() # Ask the question to the user

        for item in valid_response:

            if response == item[0] or response == item:
                return item

        print("Please enter yes / no \n") # An error will show if the item is not in the list

# Not blank function taken from MMF
def not_blank(question, error):

    while True:

        response = input(question)

        if response == "":  # If response is blank, show an error
            print(error)

        else:   # If response is not blank, return the response
            return response

# Currency formatting function taken from MMF
def currency(x):
    return "${:.2f}".format(x)

# Varible costs / fixed costs
def get_expenses(var_fixed):
    
    # Set up dictionaries and lists
        
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # Get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank. ")

        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity: ", int)

        else:
            quantity = 1

        price = num_check("How much for a single item? $", float)

        # Add to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame["Cost"] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

# Profit goal function
def profit_goal(total_costs):

    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        response = input("What is your profit goal? ")

        if response[0] == "$":
            profit_type = "$"
            amount = response[1:]

        elif response [-1] == "%":
            profit_type = "%"
            amount = response[:-1]

        else:
            profit_type = "unknown"
            amount = response

        try:
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        # Ask user if they mean $ or % depending on if response is < or > 100
        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. ie {:.2f} dollars? (y / n) ".format(amount, amount))

            if dollar_type == "yes":
                profit_type = "$"

            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}% (y / n) ".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # Return profit goal
                
        if profit_type == "$":
            return amount
        
        else:
            goal = (amount / 100) * total_costs
            return goal

# Product price rounder
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

# Instructions
def show_instructions():
    print('''\n
***** Instructions *****
          
This program will ask you for...
- The name of the product you are selling
- How many items you plan on selling
- The costs for each component of the product
- How much money you want to make
          
It will then output an itemised list of the costs
with subtotals for the variable and fixed costs.
Finaly it will tell you how much you should sell
each item for to reach your profit goal.
          
The data will be written to a text file which
has the same name as your product.

**** Program Launched! ****''')
  
# Main routine

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to see the instructions? ")
if want_instructions == "yes":
    show_instructions()

# Get product name and amount to be sold
product_name = not_blank("Product name: ", "The product name cant be blank!")
how_many = num_check("How many items will you be producing? ", int)

# Variable and fixed costs
print()
print("Please enter your variable costs below...")

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]
print()

# Get fixed costs
have_fixed = yes_no("Do you have fixed costs (y / n)? ")
if have_fixed == "yes":
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0

# Work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculate total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for number to round up to
round_to = num_check("Round to nearest...? $", int)
print()

# Calculate prices
selling_price = sales_needed / how_many
recomended_price = round_up(selling_price, round_to)

# Change dataframe to string for .txt and printing
variable_txt = pandas.DataFrame.to_string(variable_frame)

# List to make sure text written to file is the same as to terminal

# cleaner to_write list formatting
title = "**** Fund Raising - {} ****".format(product_name)
variable_print = "**** Variable Costs ****\n{}\nVariable Costs: ${:.2f}".format(variable_txt, variable_sub)

if have_fixed == "yes":
    fixed_txt = pandas.DataFrame.to_string(fixed_frame[['Cost']]) # Fixed costs dataframe is only changed to string if it exists
    fixed_print = "**** Fixed Costs **** \n{}\nFixed Costs: ${:.2f}".format(fixed_txt, fixed_sub)
else:
    fixed_print = "**** No Fixed Costs ****"

total_costs = "**** Total Costs: ${:.2f} ****".format(all_costs)
targets = "**** Profit & Sales Targets ****\n Profit Target: ${:.2f}\n Total Sales: ${:.2f}".format(profit_target, sales_needed)
pricing = "**** Pricing ****\n Minimum Price: ${:.2f}\n Recomended Price: ${:.2f}".format(selling_price, recomended_price)

to_write = [title, variable_print, fixed_print, total_costs, targets, pricing]

# Write to file
# Create .txt file to hold data
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")
# close .txt 
text_file.close()

# Print in terminal
for item in to_write:
    print(item)
    print()
import pandas

# Functions
# Number checker for floats and ints!!!
def num_check(question, num_type):

    # More detailed value error message
    if num_type == int:
        val_error = "This must be an integer! (a whole number)"

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

# Yes no checker function
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

# Varible costs
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

# Main routine

# Get product name
product_name = not_blank("product name: ", "The product name cant be blank!")

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Get fixed costs
fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]

# Printing area
print("**** Variable Costs ****")
print(variable_frame)
print()
print("Variable Costs: ${:.2f}".format(variable_sub))

print("**** Fixed Costs ****")
print(fixed_frame[['Cost']])
print()
print("Fixed costs: ${:.2f}".format(fixed_sub))
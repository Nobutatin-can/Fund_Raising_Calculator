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

want_instructions = yes_no("Do you want to see the instructions? ")
if want_instructions == "yes":
    show_instructions()
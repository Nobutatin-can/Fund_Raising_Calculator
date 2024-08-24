# Functions

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

        

# Main routine
all_costs = 200

# Testing loop
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))
    print()
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

# Main routine
print() # Check that the function works for int AND float
get_int = num_check("Enter an integer more than 0: ", int)
print("Program continues")
get_float = num_check("Enter a float more than 0: ", float)
print("Program continues")

# Display user inputs
print("This is your integer: {}".format(get_int))
print("This is your float: {}".format(get_float))
print("Program continues")

# Test what happens if num_type is invalid
get_number = num_check("Enter a number:", "int")
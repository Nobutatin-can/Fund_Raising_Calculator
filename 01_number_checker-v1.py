# Number checker for floats and ints!!!
def num_check(question, num_type, error):

    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <=  0:
                print(error)

            else:
                return response
            
        except ValueError:
            print(error)

# Main routine
print()
get_int = num_check("Enter an integer more than 0: ", int, "This is not an integer more than 0")
print("Program continues")
get_float = num_check("Enter a float more than 0: ", float,"This is not a float more than 0")
print("Program continues")

print("This is your integer more than 0: {}".format(get_int))
print("This is your float more than 0: {}".format(get_float))
# Libraries
import math

# Functions
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# Main routine
to_round = [2.91, 4.10, 6.00]

for item in to_round:
    rounded = round_up(item, 1)
    print("${:.2f} --> ${:.2f}".format(item,rounded))
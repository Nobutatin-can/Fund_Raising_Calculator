import pandas

# Frames and content for export

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Advertising"],
    "Price": [25, 35, 10]
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

# Change dataframes to string
variable_txt = pandas.DataFrame.to_string(variable_frame)
fixed_txt = pandas.DataFrame.to_string(fixed_frame)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recomended_price = "The recomended price is $5.00"

to_write = [product_name, variable_txt, fixed_txt, profit_target, required_sales, recomended_price]

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
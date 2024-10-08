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

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recomended_price = "$5.00"

print(variable_frame)

# Change dataframe to string
variable_txt = pandas.DataFrame.to_string(variable_frame)

# Write to file
# Create .txt file to hold data
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# Heading
text_file.write("**** Fund Raising - {} *****\n\n".format(product_name))

text_file.write(variable_txt)

# Close .txt file
text_file.close()
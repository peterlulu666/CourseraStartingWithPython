# Compare the current_largest_number with every number in the list
num_list = [2, 6, 96, 45, 5]
# Initialize the current_largest_number
current_largest_number = -1
# Compare number
for num_in_list in num_list:
    if num_in_list > current_largest_number:
        # If the number in the list is greater, copy the number to the current_largest_number
        current_largest_number = num_in_list
    # Print the number
    print("The current largest number is " + str(current_largest_number) + " " + "the number is list is " + str(
        num_in_list))
# Print the current_largest_number
print(current_largest_number)



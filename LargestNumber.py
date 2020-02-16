# Compare the current_largest_number with every number in the list
num_list = [2, 6, 96, 45, 5]
# Initialize the current_largest_number
current_largest_number = -1
# Compare number
for num_in_list in num_list:
    print("Compare the current largest number " + str(current_largest_number) + " with the number in list " + str(
        num_in_list))
    if num_in_list > current_largest_number:
        # If the number in the list is greater, copy the number to the current_largest_number
        current_largest_number = num_in_list
    # Print the number
    print("The current largest number is " + str(current_largest_number))
# Print the current_largest_number
print("The largest number in the list is " + str(current_largest_number))



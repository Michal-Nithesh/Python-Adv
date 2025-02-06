# Write a Python program that takes a list of strings (e.g., ["1", "2", "3"]) 
# and converts it to a list of integers. 
# Print the final list.

str_list = ["1", "2", "3"]
int_list = [int(x) for x in str_list]
print(int_list)
# Write a Python program that takes a float as input, converts it to a string, 
# and then extracts the integer part of the float using string slicing. 
# Print the result.

float_num = float(input("Enter an Float:"))
str_num = str(float_num)
int_part = str_num.split('.')[0]  # Extract integer part
print("Integer Part:", int_part)
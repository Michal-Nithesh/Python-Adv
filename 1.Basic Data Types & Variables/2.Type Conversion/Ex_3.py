# Create a Python script that takes two inputs: one integer and one float. 
# Convert the integer to a float and the float to an integer, 
# then print both converted values.

int_input = int(input("Enter an integer: "))
float_input = float(input("Enter an Float: "))

int_to_float = float(int_input)
float_to_int = int(float_input)

print("Integer to Float:", int_to_float)
print("Type of:", type(int_to_float))
print("Float to Integer:", float_to_int)
print("Type of:", type(float_to_int))
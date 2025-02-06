# Implicit Type Conversion
a = 5 + 20.6
print(type(a))

# Explicit Type Conversion
num = int("123")
print(type(num))

# Implicit Conversion
a = 10      # int
b = 5.5     # float
result = a + b  # Python automatically converts a to float
print("Implicit Conversion Result:", result)  # Output: 15.5 (float)

# Explicit Conversion
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print("Explicit Conversion Result:", num_int)  # Output: 123 (int)

# Other Examples
float_num = float("3.14")  # Convert string to float
bool_val = bool(0)         # Convert integer to boolean (False)
str_val = str(100)         # Convert integer to string
print("Float:", float_num)
print("Boolean:", bool_val)
print("String:", str_val)
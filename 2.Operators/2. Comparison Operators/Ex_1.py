# Write a program to check if a given number is greater than another number.
num_1 = int(input("Enter the value 1:"))
num_2 = int(input("Enter the value 2:"))
num_3 = int(input("Enter the value 3:"))

if num_1 > num_2 and num_1 > num_3:
    print("The greatest value is:", num_1)
elif num_2 > num_3:
    print("The greatest value is:", num_2)
else:
    print("The greatest value is:", num_3)
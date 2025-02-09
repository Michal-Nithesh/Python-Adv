# Write a program to find the largest of three numbers.

num_1 = int(input("Enter the value 1:"))
num_2 = int(input("Enter the value 2:"))
num_3 = int(input("Enter the value 3:"))

if num_1 > num_2 and num_1 > num_3:
    print("The greatest value is:", num_1)
elif num_2 > num_3:
    print("The greatest value is:", num_2)
else:
    print("The greatest value is:", num_3)
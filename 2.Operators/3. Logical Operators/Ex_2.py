# Write a Python program to check if a number is either even or divisible by 5.
number = int(input("Enter the value:"))

if number % 2 == 0 or number % 5 == 0:
    print("Success")
else:
    print("Fail")
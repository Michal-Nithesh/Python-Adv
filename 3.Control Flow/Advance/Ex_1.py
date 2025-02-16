# Write a program to print a pyramid pattern using for loops.

rows = 10

for i in range(0, rows):
    print((" " * (rows - i - 1)) + "*" * (2 * i + 1))

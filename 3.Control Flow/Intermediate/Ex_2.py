# Write a Python program to find the sum of all even numbers from 1 to 100.

sum_even_numbers = 0

for i in range(sum_even_numbers, 101):
    if i % 2 == 0:
        sum_even_numbers += i
        
print(sum_even_numbers)
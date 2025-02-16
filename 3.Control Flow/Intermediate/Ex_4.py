# Use a for loop to print all prime numbers between 1 and 50.

sum_of_prime = 0

for i in range(1, 51):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            sum_of_prime += i
            
print(sum_of_prime)
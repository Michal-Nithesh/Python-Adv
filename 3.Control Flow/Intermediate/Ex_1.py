# Print the first 10 Fibonacci numbers using a loop.

count = 1
a = 0
b = 1

while(count <= 10):
    print(a)
    temp = a
    a = b
    b = temp + b
    # a, b = b, a + b
    count += 1
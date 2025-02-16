# Implement a simple menu-driven calculator using while loop.

while True:
    options = input("Enter the option(+, -, *, /): ")
    if options in ["+", "-", "*", "/"]:
        value_1 = int(input("Enter value one: "))
        value_2 = int(input("Enter value two: "))
        if options == '+':
            print(value_1 + value_2)
        elif options == '-':
            print(value_1 - value_2)
        elif options == '*':
            print(value_1 * value_2)
        elif options == '/':
            if value_2 != 0:
                print(value_1 / value_2)
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid option. Please try again.")
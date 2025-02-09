# Implement a program that takes a user's input and keeps asking until they enter "exit".

while True:
    user_input = str(input("Enter something: "))
    if user_input == "exit":
        break
    
print("You escaped")
# Take user input for age and check if the person is eligible for voting (age >= 18).

Age = int(input("Enter the user age:"))

if Age >= 18:
    print("The person is eligible for voting")
else:
    print("The person is not eligible for voting")
# Check if a given year is a leap year using logical operators.

year = int(input("Enter the year:"))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("It's a leap year")
else:
    print("It's not a leap year")
    

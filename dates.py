#Program that asks the user to enter a month (in numeric form), a day, and a 2 digit year to see whether it is a magic date or not

# Prompt the user to enter the month, day, and year
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
year = int(input("Enter the 2-digit year (0-99): "))

# Verify the input values
if not (1 <= month <= 12) or not (1 <= day <= 31) or not (0 <= year <= 99):
    print("Invalid input. Please enter valid values.")
else:
    # Check if the date is magic
    if month * day == year:
        print(f"The date is {month} / {day} / {year}")
        print("This is a magic date.")
    else:
        print(f"The date is {month} / {day} / {year}")
        print("This is not a magic date.")

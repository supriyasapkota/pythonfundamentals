#a program that finds number of Dollars, quarters, dimes, nickels, pennies given an amount.

# Prompt the user to enter an amount
amount = float(input("Enter an amount in dollars and cents: "))

# Convert the amount to pennies (multiply by 100)
amount_in_pennies = int(amount * 100)

# Calculate the number of dollars
dollars = amount_in_pennies // 100

# Calculate the remaining amount after removing dollars
remaining_amount = amount_in_pennies % 100

# Calculate the number of quarters
quarters = remaining_amount // 25

# Calculate the remaining amount after removing quarters
remaining_amount %= 25

# Calculate the number of dimes
dimes = remaining_amount // 10

# Calculate the remaining amount after removing dimes
remaining_amount %= 10

# Calculate the number of nickels
nickels = remaining_amount // 5

# Calculate the number of pennies
pennies = remaining_amount % 5

# Display the results
print(f"Your amount {amount:.2f} consists of")
print(f"{dollars} dollars")
print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{nickels} nickels")
print(f"{pennies} pennies")

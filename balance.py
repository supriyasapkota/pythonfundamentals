#A program that will calculate the ending balance of a 1-year certificate of deposit and also verifies whether the customer is new or existing and the different rate for both type of customers.  

def main():
    # To declare the variables
    interestRate = 0.0

    # To prompt for the type of customer
    customer_type = input("Enter n if customer is new, or e for existing: ")

    # To prompt for the initial investment amount
    initial_investment = float(input("Please enter investment amount: "))

    # To check if the customer is existing and has invested >= 1000
    if customer_type == 'e' and initial_investment >= 1000:
        interestRate = 3.25
    elif customer_type == 'e':
        interestRate = 3.0
    else:
        interestRate = 3.5

    # To calculate the ending balance
    endBalance = initial_investment * (1 + interestRate / 100)

    # To display the result
    print("Interest rate = {:.2f} %".format(interestRate))
    print("Ending balance = $ {:.2f}".format(endBalance))

# Now to call the main function to start the program
main()

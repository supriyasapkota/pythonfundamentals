# A program that asks how many tickets are each class of seats were sold, then displays the amount of income generated from ticket sales.

#To declare function to get the input (category & number) from user
def getUserInput():
    category = input("Enter the category (A, B, or C): ")
    num_tickets = int(input("Enter the number of tickets required: "))
    print("Do you need more tickets?")
    need_more_tickets = input("Press Y to continue or N to quit: ")
    return category, num_tickets, need_more_tickets


#To declare function to set the seating price based on the category 
def getSeatingPrice(seat_class):
    if seat_class == 'A':
        return 20.0
    elif seat_class == 'B':
        return 15.0
    elif seat_class == 'C':
        return 10.0
    else:
        return 0.0

#to declare function to display income
def displayIncome(income_Aseats, income_Bseats, income_Cseats):
    #To display the income generated from each seating category
    print("Income from class A seats: ${:.2f}".format(income_Aseats))
    print("Income from class B seats: ${:.2f}".format(income_Bseats))
    print("Income from class C seats: ${:.2f}".format(income_Cseats))
    total_income = income_Aseats + income_Bseats + income_Cseats
    print("Total income: ${:.2f}".format(total_income))

def main():
    # To initialize income variables for each seating category
    income_Aseats = 0.0
    income_Bseats = 0.0
    income_Cseats = 0.0

    print("Welcome to the Stadium Seating Application\n")
    print("Category A - $20")
    print("Category B - $15")
    print("Category C - $10\n")

    while True:
        #To get user input for category, number of tickets, and whether to continue
        category, num_tickets, need_more_tickets = getUserInput()
        seating_price = getSeatingPrice(category)

        #To calculate the income based on the category 
        if category == 'A':
            income_Aseats += num_tickets * seating_price
        elif category == 'B':
            income_Bseats += num_tickets * seating_price
        elif category == 'C':
            income_Cseats += num_tickets * seating_price

        #To check if the user wants to continue purchasing tickets
        if need_more_tickets.upper() == 'N':
            break
    #Finally, to display the entire income summary
    displayIncome(income_Aseats, income_Bseats, income_Cseats)

# Now, to call the main function to start the program
main()

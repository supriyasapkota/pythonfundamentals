#A program that gives simple math quizzes which displays two random numbers that are to be added. Then allows the student to enter the answers and check whether it is correct or not.

import random

#To declare function to display the math problems
def displayProblem(a, b):
    print(a)
    print("+", b)

#To declare function to get the user's name
def getAnswer():
    return int(input("Enter the sum of the numbers: "))

#To declare function to calculate the correct answer
def calculateCorrectAnswer(a, b):
    return a + b

#To declare function to show the results
def showResult(correct_answer, user_answer):
    if correct_answer == user_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Incorrect... The correct answer is: {correct_answer}")
#This is the main function that displays random number
def main():
    # To declare variables
    a = random.randint(100, 999)
    b = random.randint(10, 99)

    # To display the math problem
    displayProblem(a, b)

    # To get the user's answer
    user_answer = getAnswer()

    # To calculate the correct answer
    correct_answer = calculateCorrectAnswer(a, b)

    # To show the result
    showResult(correct_answer, user_answer)

# Now, to call the main function to start the program
main()

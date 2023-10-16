#A program that uses nested loops to draw a specified pattern.

# To create a loop to iterate from 0 to 6 (i.e 7 times)
for i in range(7):
    # To print a '#' character, all on the same line
    print('#', end="")

    # To create a loop to iterate from 0 to the value of 'i' from the previous loop
    for j in range(i):
        # Print a space character, all on the same line
        print(" ", end="")

    # To print another '#' character to complete the pattern
    print("#")

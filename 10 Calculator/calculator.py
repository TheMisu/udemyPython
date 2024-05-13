# importing the calculator ASCII art
from art import logo

# defining the helper math functions
def add(num1, num2):
    """
    Function that returns the result of num1 + num2
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Function that returns the result of num1 - num2
    """
    return num1 - num2

def multiply(num1, num2):
    """
    Function that returns the result of num1 * num2
    """
    return num1 * num2

def divide(num1, num2):
    """
    Function that returns the result of num1 / num2
    """
    return num1 / num2


# defining a dictionary that stores the mathematical operations we want our calculator to use
# for example: * -> multiply or + -> add
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# writing the calculator function
def calculator():
    """
    Function that asks the user to input 2 numbers and an opertion and then returns the value of performing
    the chosen operation on the inputted numbers.
    The calculator function can be rerun multiple times using recursion. 
    """
    print(logo)

    # taking the first input
    num1 = float(input("What's the first number?: "))

    # printing the operations the user can pick
    for operation in operations:
        print(operation)

    # starting a while loop to be able to use the caluclator until we want to stop
    keep_looping = True
    while keep_looping:
        # taking input for the operation
        operation_symbol = input("Pick an operation: ")
        calc_function = operations[operation_symbol]

        # taking input for the 2nd number and performing the operation
        num2 = float(input("What's the second number?: "))
        result = calc_function(num1, num2)

        # printing the result
        print(f"{num1} {operation_symbol} {num2} = {result}")


        # asking the user if they want to continue using the current result,
        # start a new calculation or exit the program
        choice = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation or 'e' to exit: ").lower()

        if choice == "y":
            # switching num1 to result in order to be able to continue using the calculator app
            num1 = result
        elif choice == "n":
            # exit the while loop and restart the calculator function
            keep_looping = False
            calculator()
        else:
            # print Goobye and exit the while loop
            print("Goobye! ")
            keep_looping = False

# starting the program calling the calculator function 
calculator()
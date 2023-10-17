from art import logo
import os
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2;

operation_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    os.system("clear")
    print(logo)

    f_number = float(input("What's the first number?: "))

    for key in operation_dictionary:
        print(key)

    is_continue = True
    while is_continue:

        operation = input("Pick an operation: ")
        s_number = float(input("What's the next number?: "))

        calculation_function = operation_dictionary[operation]
        result = calculation_function(f_number, s_number)

        counter = input(f"Type 'y' to continue calculating with {result}, or typr 'n' to start new. ")

        if counter == 'n':
            is_continue = False
            calculator()

        else:
            f_number = result

calculator()
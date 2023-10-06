# print("Welcome to rollercoaster")
# height = int(input("Enter your height in cm? "))

# if height > 120:
#     print("You can ride")
# else:
#     print("You can't ride")

# Check given number is even or odd
# number = int(input("Enter the number: "))

# if number%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# Nested If else
height = int(input("Enter your height in cm? "))

if height > 120:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your Ticket Prive is $5")
    elif age <= 18:
        print("Your Ticket Prive is $7")
    else:
        print("Your ticker price is $12")
else:
    print("You can't ride")
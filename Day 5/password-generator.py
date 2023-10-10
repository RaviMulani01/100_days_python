import random

print("Welcome to the PyPassword Generator!")

# taking input from user for password
total_letters = int(input("How many letters would you like in your password?\n"))
total_symbol = int(input("How many symbols would you like?\n"))
total_number = int(input("How many numbers would you like?\n"))

# Store letters, number and Symbols in list
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
               '{', '}', '[', ']', '|', ';', ':', '<', '>', ',', '.', '?', '/']

# Create empty list to store password char
password_list = []

# Generate letters
for i in range(0, total_letters):
    password_list.append(random.choice(char_list))

# Generate Symbols
for i in range(0, total_symbol):
    password_list.append(random.choice(symbol_list))

# Generate Numbers
for i in range(0, total_number):
    password_list.append(random.choice(digit_list))

# Change the order of item in list
random.shuffle(password_list)

# store all item from password list to string passwird
password = ""
for char in password_list:
    password += char
    
# print final password
print(f"Here is your password: {password}")
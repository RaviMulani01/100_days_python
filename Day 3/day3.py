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
# height = int(input("Enter your height in cm? "))

# if height >= 120:
#     print("You can ride")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         price = 5
#     elif age <= 18:
#         price = 7
#     else:
#         price = 12

#     photo = input("Do you Want Photo taken? Y or N. ")

#     if(photo == "Y"):
#         price += 3

#     print(f"Your Ticket Final Price is {price}") 
    
# else:
#     print("You can't ride")

# BMI Calculator

# height = float(input("Enter Your Height in m:"))
# weight = float(input("Enter Your Weight in kg:"))
# bmi = weight / (height * height)

# if bmi <= 18.5:
#     print(f"Your BMI is {bmi}, your are underweight.")
# elif bmi <= 25:
#      print(f"Your BMI is {bmi}, your have a normal weight.")
# elif bmi < 30:
#       print(f"Your BMI is {bmi}, your are slightly overweight.")
# elif bmi < 35:
#       print(f"Your BMI is {bmi}, your are obese.")
# else:
#       print(f"Your BMI is {bmi}, your are clinically obese..")

# Leap Year cheack

# year = int(input("Enter Year:"))

# if year%4==0:
#     if year%100 == 0:
#         if year%400 == 0:      
#             print("Year is leap year")
#         else:
#             print("Year is not leap year")
#     else:
#         print("Year is leap year")
# else:
#     print("Year is not leap year")

# Pizza Order

print("Thanks for choosing our pizza shop today!")

size = input(" What size pizza you wants? S, M or L. ")
add_paneer = input("Do you want Paneer? Y or N. ")
extra_chesse = input("Do you want extra cheese? Y or N. ")
price = 0

if(size == "S"):
    price = 15
elif(size == "M"):
    price = 20
elif(size == "L"):
    price = 25
else:
    print("Pls Select valid size")

if(add_paneer == "Y"):
    if(size == "S"):
        price += 2
    elif(size == "M" or size == "L"):
        price += 3
    else:
        print("Pls Select valid size")

if(extra_chesse == "Y"):
    price += 1

print(f"Your Final Pizza Price is ${price}")

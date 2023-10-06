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

if height >= 120:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    else:
        price = 12

    photo = input("Do you Want Photo taken? Y or N. ")

    if(photo == "Y"):
        price += 3

        print(f"Your Ticket Final Price is {price}") 
    
else:
    print("You can't ride")

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
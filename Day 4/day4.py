import random

# # Genrate Random Number Beteen 0 to 4
# random_integer = random.randint(0,4)
# print(random_integer)

# # Genrate float point number. it will generate between 0.0000.. to 0.99999...
# random_float = random.random()
# print(random_float)

# # Virtual toss program.
# toss = random.randint(0,1)

# if toss == 0:
#     print("Heads")
# else:
#     print("Tails")

# # List
# fruits = ["Apple", "Banana", "Orange"]
# print(fruits)

# # add item in end
# fruits.append("Mengo")
# print(fruits)

# #add item at specific index
# fruits.insert(1, "Pinapple")
# print(fruits)

# Select random name from list

name = ["Ravi", "Manan", "Akash", "Mohit"]
bill_pay = name[random.randint(0, len(name)-1)]
print(f"{bill_pay} is going to buy the meal today!")
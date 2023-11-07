
# list = [1, 2, 3]
# # list comprehension
# new_list = [item for item in list]
# print(new_list)

# name = "Xyzs"
# new_name = [letters for letters in name]
# print(new_name)

# new_number = [n*2 for n in range(1,5)]
# print(new_number)

# # list comprehension with condition
# names = ["Alex", "Beth", "Caroline", "Dave", "Elaner", "Freddies"]
# new_number = [name.upper() for name in names if len(name) > 5]
# print(new_number)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# sequeance_numbers = [n*n for n in numbers]
# print(sequeance_numbers)

# numbers = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]
# even_number = [n for n in numbers if n%2 == 0]
# print(even_number)


# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# students = ["Alex", "Beth", "Caroline", "Dave", "Elaner", "Freddies"]
# import random
# student_score = {student:random.randint(1,100) for student in students}
# print(student_score)

# passed_student = {new_key:new_value for (new_key,new_value) in student_score.items() if new_value>35}
# print(passed_student)

sentance = input("Enter Your Sentance")

result = {word:len(word) for word in sentance.split()}
print(result)
# # Dictionary
# college = { "name": "Unknown", "total_students": 101}

# # # Retrieving items from dictionary.
# # print(college["name"])

# # Adding new items to dictionary.
# college["Adress"] = "Toronto"

# print(college)

# # # create an empty dictionary
# # empty_dictionary = {}

# # # wipe an existing dictionary
# # college = {}

# # edit an item in a dictionary
# college["Adress"] = "Canada"
# print(college)

# loop through a dictionary
# for things in college:
#     print(things+ ":-", college[things])

# # Grading Program
# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades ={}

# for student in student_score:
#     score = student_score[student]

#     if score > 90:
#         student_grades[student] = "Outstanding"

#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"

#     elif score >70:
#         student_grades[student] = "Acceptable"

#     else:
#         student_grades[student] = "Fail"

# for score in student_grades:
#     print(score,":",student_grades[score])

# # Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# # Nesting a list in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijion"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# ["a", "b", ["c", "d"]]

# # Nesting a dictionary in a Dictionary
# total_visit = {
#     "France":{
#         "Paris": 2,
#         "Lille": 4,
#         "Dijion": 3
#     }
# }

travel_log = [{
    "country": "france",
    "visits": 12,
    "cities": ["paris", "lille", "Dijon"]
    },

    {
    "country": "germany",
    "visits": 5,
    "cities": ["berlin", "hamburg", "stuttgart"]  
    }
]

def add_new_country(country, visits, list_of_cities):
    travel_log.append({"country": country, "visits": visits, "cities": list_of_cities})

print("Before")
print(travel_log)

add_new_country("canada", 4, ["Toronto", "Brampton", "Mississauga"])

print("After")
print(travel_log)
# # function with return value
# def format_name(f_name,l_name):\

#     if f_name == "" or l_name == "":
#         return "Pls provide valid inputs."
        
#     formeted_f_name = f_name.title()
#     formeted_l_name = l_name.title()
#     return f"{formeted_f_name} {formeted_l_name}"

# name = format_name("", "mulani")
# print(name)

# # Days in Month

# # create function to check for leep year
# def is_leap(year):
#     if year % 4 == 0:  
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# # return the number of days in the given year and month
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     if month == 2 and is_leap(year):
#         return 29
    
#     return month_days[month-1]

# # taking user input
# year = int(input("Enter Year: "))
# month = int(input("Enter Month: "))

# # calculate total days in month
# days = days_in_month(year,month)
# print(days)
name = input("Enter your name: ")
print("Your name length is:", len(name))

name1 = input("Enter First Name: ")
name2 = input("Enter Secound Name: ")

print("\nBefor Swapping")
print("First Name: ", name1, "\nSecound Name: ", name2)

#Swap two variables
temp = name1
name1 = name2
name2 = temp

print("\nAfter Swaaping")
print("First Name: ", name1, "\nSecound Name: ", name2)
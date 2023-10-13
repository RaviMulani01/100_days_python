# # Sum of two number
# def sum(a,b):
#     print(a+b)

# sum(int(input("Enter first number: ")), int(input("Enter secound number: ")))

# # print great by user name
# def great(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# great(input("Enter Your Name: "))

# # function with keyword arguments
# def great_with(name, location):
#     print(f"Hello {name}")
#     print(f"How's in {location}")

# great_with(name="NOBODY", location="Computer")
# # both are same with argument value else it not same
# # great_with(location="Computer", name="NOBODY")

# check number is prime or not
def prime_number(n):
    
    if n <= 0:
        is_prime = False
    
    else:
        is_prime = True
        for i in range(2, n):
            if n % i ==0:
                is_prime = False
        
    print("Number is Prime: ", is_prime)

prime_number(int(input("Enter Number for check prime number or not: ")))


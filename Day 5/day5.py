# # for loops
# fruits = ["Apple", "Banana", "Mango"]

# for fruit in fruits:
#     print(fruit)

# # For loop with rang
# for i in range(1,10):
#     print(i)

# Sum of even number with range funtion
# target = int(input())

# sum = 0
# for i in range(2, target+1,2):
#     sum += i
# print(sum)

# the FizzBuzz to print 1 to 100

for i in range(1,101):

    if i%3==0 and i%5==0:
        print("FizzBuzz")
    
    elif i%3 == 0:
        print("Fizz")

    elif i%5 == 0:
        print("Buzz")
    
    else:
        print(i)
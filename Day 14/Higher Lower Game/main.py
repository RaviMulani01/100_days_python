import random
import art
import game_data
import os

print(art.logo)
# create function to check who has more followers
def check_follower(a, b, user_choice):
    if a['follower_count'] > b['follower_count'] and user_choice=="a":
        return True 
    elif b['follower_count'] > a['follower_count'] and user_choice=="b":
        return True     
    else:
        return False

# generate random person
b = random.choice(game_data.data)

# count the number of currect guess
count = 0

# create a while loop to run untill user guess all correct guess.
result = True
while result:
    
    # assign a = b for next rount b become a.
    a = b

    b = random.choice(game_data.data)
    # check for both person not same
    if a == b:
        b = random.choice(game_data.data)

    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']}")

    # taking user guess
    your_choice = input("who has more followers? Type 'A' or 'B': ").lower()

    # clear the screen using os module
    os.system('clear')
    print(art.logo)

    # check for guess is correct or not!
    if not check_follower(a,b,your_choice):
        print("Sorry, that's wrong. Final Score: ", count)
        result = False

    else:
        count+=1
        print(f"You're right! Current Score: {count}.")
        
















    # if your_choice == "a":
    #     if a['follower_count'] > b['follower_count']:
    #         print("you win")
    #         count+=1
    #     else:
    #         print("Sorry, that's wrong. Final Score: ", count)
    #         result = False

    # else:
    #     if b['follower_count'] > a['follower_count']:
    #         print("You win")
    #         count+=1
        
    #     else:
    #         print("Sorry, that's wrong. Final Score: ", count)
    #         result = False
    


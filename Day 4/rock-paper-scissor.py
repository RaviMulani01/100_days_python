import random

# Rock Paper Scissors ASCII Art
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Strore all symbol value in list
list_choice = [rock, paper, scissors]

# taking user choice
our_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if our_choice > 2 or our_choice < 0:
    print("Invalid Number!! you lose.")

else:
    print(f"Your Choice: {list_choice[our_choice]}")

    # genrate computer choice using random function
    compter_choice = random.randint(0,2)
    print(f"Computer Choice: {list_choice[compter_choice]}")

    if our_choice == compter_choice:
        print("Draw")

    elif our_choice == 0:
        if compter_choice != 2:
            print("You lose")
        else:
            print("You win.")

    elif our_choice == 1:
        if compter_choice != 0:
            print("You lose.")
        else:
            print("You win.")

    elif our_choice == 2:
        if compter_choice != 1:
            print("You lose.")
        else:
            print("You win.")

    print("\n")
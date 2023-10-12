import random
import hangman_art
import hangman_word
import os

# Give total lives for hangman
hangman_life = 5

# print logo from hangman_art file
print(hangman_art.logo)

# genrate random word from the list
chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)
print(chosen_word)

# initializing list with random word length
display = []
for i in range(0, word_length):
    display.append("_")    # display += "_"
print(f"{' '.join(display)}")

# while loop until all _ not fill
end_of_game = False
while not end_of_game:
    
    # taking user guess
    guess = input("Guess a letter: ").lower()

    # clear the previous screen
    os.system('clear')

    # replace _ with letter if it is present in words
    if guess in chosen_word:
        
        # check if guess letter is already guessed
        if guess in display:
            print(f"you've already guessed {guess}")

        else:
            for i in range(0, word_length):
                # Replace "_" with guess letter
                if chosen_word[i] == guess:
                    display[i]=guess
        

    # if letter not present display hangman
    else:  

        if(hangman_life > 0):
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(hangman_art.stages[hangman_life])
            hangman_life -= 1

        else:
            print(hangman_art.stages[hangman_life])
            print("Game Over")
            break

    print(f"{' '.join(display)}")

    # check condition untill any black position
    if "_" not in display:
        end_of_game = True
        print("You Win!")

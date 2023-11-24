# Random module that randomises the words for the game
import random
# importing the wordlist.py to be used in the game
from wordlist import word_list


# Defined word to be chosen from wordlist and making the words uppercase
def get_word():
    word = random.choice(word_list)
    return word.upper()


# Defining the play function
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    # Player's username
    user_name = input("Your name: ")
    print(f"Welcome {user_name}! Let's play!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Start playing! Choose your first letter. You have 7 tries before x_x")
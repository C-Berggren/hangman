import random
from wordlist import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7

# Player's username
user_name = input("Your name: ")
print(f"Welcome {user_name}! Let's play!")
print("Start playing! Choose your first letter. You have 7 tries before x_x")
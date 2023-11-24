# Random module that randomises the words for the game
import random
# the game's word list
word_list = [
    'meat'
    'waggish'
    'unit'
    'snotty'
    'flock'
    'office'
    'race'
    'bite'
    'giant'
    'nervous'
    'chess'
    'embarrassed'
    'rush'
    'judicious'
    'temper'
    'frail'
    'elderly'
    'hellish'
    'beautiful'
    'malicious'
    'friction'
    'check'
    'available'
    'eyes'
    'cloudy'
    'river'
    'zebra'
    'turkey'
    'warn'
    'lopsided'
    'look'
    'habitual'
    'innate'
    'agree'
    'harmony'
    'average'
    'jealous'
    'entertaining'
    'ultra'
    'disagreeable'
    'loss'
    'momentous'
    'bewildered'
    'bee'
    'toys'
    'confuse'
    'vengeful'
    'blood'
    'lacking'
    'defiant'
    'outrageous'
    'stereotyped'
    'haircut'
    'envious'
    'complex'
    'berry'
    'shallow'
    'marked'
    'eatable'
    'unadvised'
    'impulse'
    'adventurous'
    'unfasten'
    'waste'
    'tame'
    'gigantic'
    'subtract'
    'ban'
    'fascinated'
    'needy'
    'murder'
    'defective'
    'expert'
    'separate'
    'bump'
    'depend'
    'hands'
    'yell'
    'houses'
    'school'
    'crook'
    'scintillating'
    'type'
    'ghost'
    'dirty'
    'half'
    'harbor'
    'dolls'
    'tacky'
    'remove'
    'hose'
    'equal'
    'magic'
    'wash'
    'jelly'
    'sky'
    'breathe'
    'parched'
    'industry'
    'two'
]


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
    # Printing the Start gameplay
    print(f"Welcome {user_name}! Let's play!")
    print(word_completion)
    print("\n")

    # while loop to check your guesses are alphabetial and single or word
    while not guessed and tries > 0:
        guess = input("Start playing! Choose your first letter: ")
        print("You have 7 tries before x_x")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is in the word. Well done!")
                guessed_letters.append(guess)
                if "_" not in word_completion:
                    guessed = True
                    print(word, f"was correct {user_name}! You survived!")
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed this word", guess)
            elif guess not in word:
                print(guess, "was the wrong word")
        else:
            print("Incorrect, please try again")
        print(word_completion)
        print("\n")

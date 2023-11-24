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

failed = 7
letter_count = ""
word = random.choice(word_list)

# Player's username
user_name = input("Your name: ")
# Printing the Start gameplay
print(f"Welcome {user_name}! Let's play!")

while failed > 0:
    guess = input("Guess a letter: ")

    if guess in word:
        print(f"Correct. There is one or more {guess} in the word")
    else:
        failed -= 1
        print(f"Incorrect. There is no {guess} in the word")

    letter_count = letter_count + guess

    for letter in word:
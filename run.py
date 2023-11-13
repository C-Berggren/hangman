# Player's username
user_name = input("Your name: ")
print(f"Welcome {user_name}! Let's play!")
print("Start playing! Choose your first letter. You have 7 tries before x_x")

# Program will choose one of the words from the list
word_list = ["secret", "human", "baby", "dog", "brilliant", "joyful", "wonder", "kitten", "friend"]

# For dev
secret_word = "brunch"

# Number of guesses
guesses = ""

# Counter of turns
turns = 7

# while loop to check number of tries versus number of turns
while turns > 0:
    # failed counter
    failed = 0

    if char in guesses:
        print(char,end="")

        else:
            print("_",end="")
            failed += 1
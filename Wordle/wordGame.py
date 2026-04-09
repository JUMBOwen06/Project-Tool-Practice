import random   

# Load answers as list
with open("answers.txt") as f:
    answers = [w.strip().upper() for w in f if w.strip()]

# Load valid words as set
with open("valid_words.txt") as f:
    valid_words = set(w.strip().upper() for w in f if w.strip())


# Global variables
word = random.choice(answers) # Choose a random word from the list
attempts = 6    # How many attempts you have to guess the word
guesses = []    # Array of the past guesses
results = []    # Array of the results for the guesses
attempt = 0     # Keep track of the current attempt
keyboard = {}   # Implementing in the future


# Compares each letter to the answer
def evaluate_word(userGuess, word):
    wordChars = list(word)      # Create a list of each char from the answer
    result = ["absent"] * len(word)     # Create an array the length of the word

    # Pass through the word twice
    # Pass 1: correct
    for i in range(len(word)):
        if userGuess[i] == word[i]:
            result[i] = "correct"
            wordChars[i] = None

    # Pass 2: present
    for i in range(len(word)):
        if result[i] == "correct":
            continue
        
        if userGuess[i] in wordChars:
            result[i] = "present"
            wordChars[wordChars.index(userGuess[i])] = None

    return result



# Loop until the game ends
while attempt < attempts:
    guess = input("Enter guess: ").upper()

    if guess not in valid_words:
        print("Not a valid word")
        continue

    # Ensure the guess is 5 letters long
    if len(guess) != 5 or not guess.isalpha():
        print("Invalid guess. Try again.")
        continue
    
    # Check past guesses
    if guess in guesses:
        print("You already guessed that.")
        continue

    result = evaluate_word(guess, word)

    # Store the guess info
    guesses.append(guess)
    results.append(result)

    print(result)

    # If the guess is right end the game
    if all(r == "correct" for r in result):
        print("You win!")
        break

    attempt += 1

else:
    print("You lose! The word was:", word)

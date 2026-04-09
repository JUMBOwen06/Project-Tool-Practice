import random  

from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.table import Table
from rich import box

# Rich theme for coorect/incorrect letters
wordle_theme = Theme({
    "correct": "bold white on green",
    "present": "bold black on yellow",
    "absent": "white on grey23"
})

console = Console(theme = wordle_theme)


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


# Shows the keboard - Indicating correct and incorrect letters
def render_board(guesses, results):
    table = Table(show_header=False, box=box.SIMPLE, pad_edge=False)

    # Create 5 columns
    for _ in range(5):
        table.add_column(justify = "left", width = 3)

    # Fill rows
    for i in range(6):  # 6 attempts
        if i < len(guesses):
            guess = guesses[i]
            result = results[i]

            row = []
            for j in range(5):
                letter = guess[j]
                style = result[j]
                cell = Text(f" {letter} ", style=style)
                row.append(cell)

            table.add_row(*row)
        else:
            table.add_row(*[" "]*5)

    console.print(table)



# Updates the used letters on the keyboard
def update_keyboard(keyboard, guess, result):
    for i in range(len(guess)):
        letter = guess[i]
        status = result[i]

        # Applies the correct state to the keys
        if letter not in keyboard:
            keyboard[letter] = status
        elif status == "correct":
            keyboard[letter] = "correct"
        elif status == "present" and keyboard[letter] != "correct":
            keyboard[letter] = "present"



# Show the keyboard
def render_keyboard(keyboard):
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

    for row in rows:
        line = []
        for letter in row:
            style = keyboard.get(letter, "")

            # Applies the correct color to the keys
            if style:
                line.append(f"[{style}] {letter} [/{style}]")
            else:
                line.append(f" {letter} ")

        console.print(" ".join(line))



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
    guess = input("\n\nEnter guess: ").upper()

    # Ensure the guess is 5 letters long
    if len(guess) != 5 or not guess.isalpha():
        print("Invalid guess. Try again.")
        continue
    
    if guess not in valid_words:
        print("Not a valid word")
#        print("DEBUG: words loaded =", len(valid_words))
        continue

    # Check past guesses
    if guess in guesses:
        print("You already guessed that.")
        continue

    result = evaluate_word(guess, word)
    update_keyboard(keyboard, guess, result)

    # Store the guess info
    guesses.append(guess)
    results.append(result)

    # Print the ui to the console
    console.clear()
    console.print()
    render_board(guesses, results)
    render_keyboard(keyboard)
    

    # If the guess is right end the game
    if all(r == "correct" for r in result):
        print("You win!")
        break

    attempt += 1

else:
    print("You lose! The word was:", word)



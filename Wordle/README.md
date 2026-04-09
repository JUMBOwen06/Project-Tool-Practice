# Wordle Clone
Terminal-Based Word Guessing Game

This project is a simple terminal-based clone of the Wordle game, built in Python.

This project is part of a series of smaller exercises designed to learn new Python
libraries and strengthen programming fundamentals before integrating them into
larger applications.

## Features
Random word selection from a text file
6 attempts to guess the correct word
Letter-by-letter feedback system:
correct — correct letter in the correct position
present — correct letter in the wrong position
absent — letter not in the word or overused
Input validation (must be 5 alphabetic characters)
Prevents duplicate guesses
Tracks guess history and results
Game Logic

The word evaluation system uses a two-pass approach:

Pass 1 — Correct Letters
Letters in the correct position are marked as correct and removed from consideration.

Pass 2 — Present Letters
Remaining letters are checked against unused letters in the word:

If found > present
If not > absent

This ensures accurate handling of duplicate letters.

## How It Works
Load a list of words from wordList.txt
Randomly select a word as the answer
Prompt the user to enter guesses
Evaluate each guess and return feedback
End the game when:
The word is guessed correctly, or
The player runs out of attempts


## File Structure

wordle/
>-- wordGame.py
>-- valid_words.txt
>-- answers.txt
>-- README.md

## Word List Format

The word list must follow these rules:

One word per line
All words must be 5 letters long
No spaces or commas

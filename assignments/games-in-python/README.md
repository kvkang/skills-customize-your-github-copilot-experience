# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice working with strings, loops, conditionals, and user input to create a complete game experience.

## 📝 Tasks

### 🛠️	Build Core Hangman Gameplay

#### Description
Create the main game loop for Hangman. The game should choose a random word, let the player guess one letter at a time, and display progress after each guess.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Ask the player to enter a single letter on each turn.
- Display the current word progress using underscores for unknown letters (for example: `_ a _ _ m a n`).
- Reveal all matching positions when the guessed letter appears in the word.
- Keep accepting guesses until the word is fully revealed or attempts run out.


### 🛠️	Track Attempts and End States

#### Description
Add game rules for incorrect guesses and finish the game with clear win or lose messages.

#### Requirements
Completed program should:

- Start with a fixed number of incorrect attempts (for example, 6).
- Decrease remaining attempts only when the guessed letter is not in the word.
- Show the player how many incorrect attempts remain after each turn.
- End the game with a win message when all letters are guessed.
- End the game with a lose message when attempts reach zero and reveal the correct word.

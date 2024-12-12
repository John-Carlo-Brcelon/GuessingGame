JOHN CARLO M. BARCELON
BSIT 2104 
TITLE: WORD GUESSING GAME
YOUTUBE URL: 


Overview

This is a Word Guessing Game built using Python's tkinter for the graphical user interface (GUI). Players must guess a word based on its definition, with different difficulty levels and categories available. The game features a timed challenge where players can make multiple attempts to guess the correct word.


Features

Difficulty Levels: The game offers four difficulty levels—Easy, Intermediate, Hard, and Difficult. The time limit for guessing changes based on the selected level:

Easy: 25 seconds

Intermediate: 20 seconds

Hard: 15 seconds

Difficult: 10 seconds

Categories: Each difficulty level has several categories like Animals, Places, Fruits, and Random words.

Word Templates: Words are presented with some letters hidden, and players must guess the full word.

Timed Challenge: A countdown timer shows how much time remains to guess the word. If time runs out or attempts are exhausted, the game moves to the next word.

Score System: Players accumulate points for every correct guess and can track their score throughout the game.

Input Validation: Players are restricted to alphabetic inputs, ensuring valid guesses.


Usage

1. Run the game: Execute the Python script to start the game.

python word_guessing_game.py

2. Main Menu: After launching the game, you'll be prompted with a splash screen, followed by the main menu where you can:

    - Start a new game

    - Exit the game

3. Choose Difficulty: Upon starting the game, select your desired difficulty level (Easy, Intermediate, Hard, or Difficult).

4. Guess the Word: Each word is displayed with its definition, and you must guess the word. Type your guess and press Enter or click Submit.

5. Time Limit: A timer will count down the available time for each word.

6. Attempts: You have 5 attempts to guess the word correctly. After 5 incorrect guesses, the correct word will be revealed.

7. Game Over: At the end of the game, your final score will be displayed, and you can return to the main menu.


Game Flow
  - Splash Screen: Displays the title of the game.
  - Main Menu: Offers options to start or exit the game.
  - Level Selection: Choose a difficulty level to play.
  - Game: Each word will be shown with a definition and a template. You must guess the word within the given time and attempts.
  - Score: Your score is displayed at the end of the game based on how many correct guesses you made.


Files

1. word_bank: A dictionary containing words and their definitions for each difficulty level and category. These words are saved into CSV files for easy access.
2. word_guessing_game.py: The main Python file that runs the game.


Customizing the Game

1. Word Bank: You can modify the word_bank dictionary to add more categories or words.
2. GUI: The game uses tkinter to create the graphical interface. Feel free to modify the layout or design as per your preference.

https://www.youtube.com/watch?v=15-83T0RWko

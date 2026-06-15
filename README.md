# Number Guessing Game (CLI)

1. PROJECT OVERVIEW
NumberGuessPro is an interactive command-line guessing game built in Python using the `random` module. It demonstrates the fundamental pipeline of game logic, user input handling, and state management. The game uses difficulty levels + smart hints + high score tracking for enhanced gameplay.

This project satisfies the "TASK 2 SPECIFICATION: NUMBER GUESSING GAME (CLI)" requirements for an interactive guessing system with hint feedback.

2. FEATURES & REQUIREMENTS MET

GENERATE RANDOM NUMBER: `random.randint()` creates target number per difficulty
ALLOW MULTIPLE ATTEMPTS: Limited attempts based on difficulty: 5 to 10
HINT SYSTEM: Too high / Too low feedback + Hot/Cold proximity hints
COUNT ATTEMPTS: Attempt counter displayed each round
GAME ENDS: Terminates on correct guess OR when attempts run out
ENHANCEMENT: 4 difficulty levels + high scores + odd/even hint + color UI

3. HOW TO RUN

Prerequisites:
- Python 3.9+ installed

Steps:
1. Open terminal and run: python number_guess_pro.py
2. Enter your name when prompted
3. Select difficulty: Easy, Medium, Hard, or Insane
4. Guess the number. Type 'hint' for odd/even hint (costs 1 attempt)
5. View high scores from main menu

4. PROJECT STRUCTURE

number_guessing_cli/
├── number_guess_pro.py - Main game logic + menu system
├── guess_highscores.json - Auto-generated high scores file
└── README.md - This file

5. HOW IT WORKS - THE IPO MODEL
1. Input: `input()` captures player name, difficulty, and guesses
2. Process: `random.randint()` generates target. Compares guess vs target. `get_smart_hint()` calculates distance
3. Output: Color-coded hints display. High score saved to JSON if record beaten

6. KEY CONCEPTS DEMONSTRATED
1. Randomization: `random.randint()` ensures unpredictable gameplay
2. Control Flow: While loop + if/elif manages game state and attempts
3. Data Persistence: JSON file stores high scores across sessions
4. Input Validation: Try/except + range checking prevents crashes
5. Game Design: Difficulty scaling + smart hints improve user experience
6. State Management: Tracks attempts, scores, and game over conditions


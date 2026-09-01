# Hangman

A classic Hangman game built with Python and Streamlit.

## Project Overview

This project is a web-based implementation of the classic Hangman game.
The player has to guess a hidden word letter by letter before making six mistakes.

The project was mainly created to practice **Python programming, application logic, and Streamlit**.

## Features

* Randomly selected words
* German QWERTZ keyboard layout
* Interactive letter buttons
* Already guessed letters are automatically disabled
* Visual Hangman progression
* Win and lose conditions
* Option to start a new game
* Game state maintained with Streamlit Session State

## Technologies

* Python
* Streamlit

## Project Structure

```text
Hangman/
│
├── main.py
├── hangman_functions.py
├── hangman_words.py
├── hangman_pics.py
└── README.md
```

### `main.py`

Contains the Streamlit application and game logic.

### `hangman_functions.py`

Contains helper functions used to process and display the hidden word.

### `hangman_words.py`

Contains the word list used by the game.

### `hangman_pics.py`

Contains the ASCII representations of the Hangman states.

## How It Works

At the beginning of each game, a random word is selected from the word list.

The selected word is hidden from the player:

```text
_ _ _ _ _ _
```

The player then selects letters using the on-screen keyboard.

* **Correct guess:** The letter is revealed in the word.
* **Incorrect guess:** The Hangman progresses by one step.
* **Six mistakes:** The player loses.
* **All letters guessed:** The player wins.

The current game state is stored using Streamlit's `session_state`, allowing the game to persist between Streamlit reruns.

## Run Locally

Install the required dependency:

```bash
pip install streamlit
```

Then start the application:

```bash
streamlit run main.py
```

The game will open in your browser.

## What I Practiced

This project helped me practice:

* Python control flow
* Functions and modular code
* Sets and lists
* Random selection
* State management with `st.session_state`
* Interactive Streamlit widgets
* Building a simple web interface with Streamlit
* Structuring a small Python project

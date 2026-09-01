import random
import hangman_functions
import hangman_words
import hangman_pics
import streamlit as st


keyboard = [
    ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Y", "X", "C", "V", "B", "N", "M"]
]

if "hidden_word" not in st.session_state:
    st.session_state.hidden_word = random.choice(
        hangman_words.wordlist
    ).lower()

    st.session_state.word = hangman_functions.spacing(
        hangman_functions.crypt(
            st.session_state.hidden_word
        )
    )

    st.session_state.guessed_letters = set()
    st.session_state.mistakes = 0
    st.session_state.game_over = False
    st.session_state.won = False


hidden_word = st.session_state.hidden_word

def make_guess(guess):

    if guess in st.session_state.guessed_letters:
        return

    st.session_state.guessed_letters.add(guess)

    if guess in hidden_word:

        st.session_state.word = (
            hangman_functions.replace_letter(
                st.session_state.word,
                hidden_word,
                guess
            )
        )

        if st.session_state.word == hidden_word:
            st.session_state.won = True
            st.session_state.game_over = True

    else:

        st.session_state.mistakes += 1

        if st.session_state.mistakes >= 6:
            st.session_state.game_over = True

st.title("Hangman")

st.code(
    hangman_pics.hangmanpics[
        st.session_state.mistakes
    ]
)

st.code(st.session_state.word.upper())

if not st.session_state.game_over:

    for row in keyboard:

        cols = st.columns(len(row))

        for col, letter in zip(cols, row):

            with col:

                disabled = (
                    letter.lower()
                    in st.session_state.guessed_letters
                )

                if st.button(
                    letter,
                    key=f"key_{letter}",
                    disabled=disabled
                ):

                    make_guess(letter.lower())

                    st.rerun()


if st.session_state.won:

    st.success("You won! 🎉")

elif st.session_state.mistakes >= 6:

    st.error("You lose!")

    st.write(
        f"The hidden word was: {hidden_word}"
    )


if st.button("New Game"):

    st.session_state.clear()
    st.rerun()
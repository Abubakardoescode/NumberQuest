import streamlit as st
import random

def guessing_game():
    secret_number = random.randint(1, 50)
    attempts_left = 5
    game_over = False

    while attempts_left > 0 and not game_over:
        # Generate a unique ID for the text input widget
        unique_id = st.session_state.get("guess_input_id", 0) + 1
        st.session_state["guess_input_id"] = unique_id

        guess_str = st.text_input(label="Guess the number (between 1 and 50). You have {} attempts left.".format(attempts_left),
                                   key=unique_id)  # Use the unique ID as a key

        try:
            guess = int(guess_str)
        except ValueError:
            st.error("Invalid input! Please enter a valid number.")
            continue

        # ... rest of the game logic ...

st.title("Guessing Game")
st.write("Try to guess the secret number between 1 and 50 in 5 attempts!")
guessing_game()

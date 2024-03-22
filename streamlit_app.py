import streamlit as st
import random as rd

def number_quest():
    st.title("Number Quest")
    st.text("Guess a number between 1 - 50")

    # Initialize session state
    if 'attempts_left' not in st.session_state:
        st.session_state.attempts_left = 5
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = rd.randint(1, 50)

    # Main game loop
    while st.session_state.attempts_left > 0:
        try:
            guess = st.number_input("Guess a Number", min_value=1, max_value=50, value=1, step=1, key="guess_input")
            button_clicked = st.button("Submit", key="submit_button")
            
            if button_clicked:
                if guess == st.session_state.secret_number:
                    st.write(f"Congratulations! You guessed the secret number {st.session_state.secret_number} correctly!")
                    return guess  # Return the guessed number
                elif guess < st.session_state.secret_number:
                    st.write(f"Try again! Your guess is too low. You have {st.session_state.attempts_left - 1} attempts left.")
                else:
                    st.write(f"Try again! Your guess is too high. You have {st.session_state.attempts_left - 1} attempts left.")
                
                if 1 <= guess <= 50:  # Only deduct attempts if guess is within the valid range
                    st.session_state.attempts_left -= 1
                
                if st.session_state.attempts_left == 0:
                    st.write(f"Game Over! The secret number was {st.session_state.secret_number}. Better luck next time!")
                    return None  # Return None when game is over
        except:
            pass  # Suppress any errors

# Start the game
guessed_number = number_quest()

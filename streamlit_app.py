import streamlit as st
import random as rd

def number_quest():
    st.title("Number Quest")
    st.text("Welcome to 'Number Quest'!")
    st.text("Can you figure out the secret number hidden between 1 and 50?")
    st.text("You have 5 attempts to guess it right.")
    st.text("Enter your guess in the box below and click 'Submit' to see if you've cracked the code.")
    st.text("Good luck!")

    # Initialize session state
    if 'attempts_left' not in st.session_state:
        st.session_state.attempts_left = 5
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = rd.randint(1, 50)

    # Main game loop
    while st.session_state.attempts_left > 0:
        try:
            guess = st.number_input("Guess a Number between 1 to 50", value=1, step=1, key="guess_input")
            button_clicked = st.button("Submit", key="submit_button")
            
            if button_clicked:
                if guess < 1 or guess > 50:
                    st.write("Please enter a number between 1 and 50.")
                    continue
                
                if guess == st.session_state.secret_number:
                    st.write(f"Congratulations! You guessed the secret number {st.session_state.secret_number} correctly!")
                    return guess  
                elif guess < st.session_state.secret_number:
                    st.write(f"Try again! Your guess is too low. You have {st.session_state.attempts_left - 1} attempts left.")
                else:
                    st.write(f"Try again! Your guess is too high. You have {st.session_state.attempts_left - 1} attempts left.")
                
                st.session_state.attempts_left -= 1
                
                if st.session_state.attempts_left == 0:
                    st.write(f"Game Over! The secret number was {st.session_state.secret_number}. Better luck next time!")
        except:
            pass  # Suppress any errors

    guessed_number = number_quest()

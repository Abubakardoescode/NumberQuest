import streamlit as st
import random

def play_guessing_game():
    st.write("Welcome to the Guess the Number game!")
    st.write("I've picked a number between 1 and 50. You have 5 attempts to guess it!")

    # Generate a random number between 1 and 50
    number_to_guess = random.randint(1, 50)
    
    attempts = 0
    max_attempts = 5
    game_over = False

    while attempts < max_attempts and not game_over:
        guess = st.text_input("Enter your guess:")

        if st.button("Submit"):
            # Check if the input is a valid number
            if not guess.isdigit():
                st.write("Invalid input! Please enter a valid number.")
            else:
                guess = int(guess)
                attempts += 1

                # Check if the guess is correct
                if guess == number_to_guess:
                    st.write("Congratulations! You've guessed the number.")
                    game_over = True
                elif attempts == max_attempts:
                    st.write(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")
                    game_over = True
                elif guess < number_to_guess:
                    st.write("Try a higher number.")
                else:
                    st.write("Try a lower number.")

    if game_over:
        if st.button("Restart"):
            play_guessing_game()

if __name__ == "__main__":
    play_guessing_game()

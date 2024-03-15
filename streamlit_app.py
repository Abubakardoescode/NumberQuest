# Import necessary libraries
from random import randint
import streamlit as st

def main():
    st.title("Guess the Secret Number Game")
    st.write("Welcome! Try to guess the secret number between 1 and 50.")

    # Generate a random secret number
    secret_number = randint(1, 50)
    attempts_left = 5

    while attempts_left > 0:
        try:
            # Get user input
            user_guess = int(st.text_input("Enter your guess:", key="guess"))

            # Check if the guess is correct
            if user_guess == secret_number:
                st.success(f"Congratulations! You guessed the secret number {secret_number} correctly!")
                break
            elif user_guess < secret_number:
                st.warning(f"Try again! Your guess is too low. You have {attempts_left} attempts left.")
            else:
                st.warning(f"Try again! Your guess is too high. You have {attempts_left} attempts left.")

            attempts_left -= 1
        except ValueError:
            st.error("Invalid input! Please enter a valid number.")

    # If user runs out of attempts
    if attempts_left == 0:
        st.error(f"Game Over! The secret number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    main()

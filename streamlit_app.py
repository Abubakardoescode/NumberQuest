import streamlit as st
import random

def play_guessing_game():
    secret_number = random.randint(1, 50)
    attempts_left = 5
    st.write("Welcome to the Guessing Game!")

    while attempts_left > 0:
        guess_text = st.text_input("Guess the secret number (between 1 and 50):")
        
        try:
            guess = int(guess_text)
            if guess < 1 or guess > 50:
                raise ValueError
        except ValueError:
            st.error("Invalid input! Please enter a valid number between 1 and 50.")
            continue

        if guess == secret_number:
            st.success(f"Congratulations! You guessed the secret number {secret_number} correctly!")
            break
        elif guess < secret_number:
            st.warning(f"Try again! Your guess is too low. You have {attempts_left - 1} attempts left.")
        else:
            st.warning(f"Try again! Your guess is too high. You have {attempts_left - 1} attempts left.")
        attempts_left -= 1

        if attempts_left == 0:
            st.error(f"Game Over! The secret number was {secret_number}. Better luck next time!")
            break

def main():
    st.title("Guess the Number Game")
    play_guessing_game()

if __name__ == "__main__":
    main()

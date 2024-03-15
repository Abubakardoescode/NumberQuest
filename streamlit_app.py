import streamlit as st
from random import randint

def play_game(secret_number):
    attempts_left = 5

    while attempts_left > 0:
        try:
            guess = st.number_input("Guess the secret number (between 1 and 50):", min_value=1, max_value=50)
        except ValueError:
            st.write("Invalid input! Please enter a valid number.")
            continue
        
        if guess == secret_number:
            st.write(f"Congratulations! You guessed the secret number {secret_number} correctly!")
            break
        elif guess < secret_number:
            st.write(f"Try again! Your guess is too low. You have {attempts_left - 1} attempts left.")
        else:
            st.write(f"Try again! Your guess is too high. You have {attempts_left - 1} attempts left.")
        
        attempts_left -= 1

    if attempts_left == 0:
        st.write(f"Game Over! The secret number was {secret_number}. Better luck next time!")

def main():
    st.title("Guess the Number Game")
    secret_number = randint(1, 50)
    play_game(secret_number)

if __name__ == "__main__":
    main()

import streamlit as st
from random import randint

def play_game(secret_number, attempts_left):
    guess = st.number_input("Guess the secret number (between 1 and 50):", min_value=1, max_value=50)
    
    if guess == secret_number:
        st.success(f"Congratulations! You guessed the secret number {secret_number} correctly!")
        return True
    elif guess < secret_number:
        st.warning(f"Try again! Your guess is too low. You have {attempts_left - 1} attempts left.")
    else:
        st.warning(f"Try again! Your guess is too high. You have {attempts_left - 1} attempts left.")
    
    return False

def main():
    st.title("NumberQuest: The Secret Number Challenge")
    secret_number = randint(1, 50)
    attempts_left = 5

    st.write("Welcome to NumberQuest! Can you guess the secret number?")
    st.write("You have 5 attempts. Good luck!")

    game_over = False
    while attempts_left > 0 and not game_over:
        game_over = play_game(secret_number, attempts_left)
        attempts_left -= 1

    if not game_over:
        st.error(f"Game Over! The secret number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    main()


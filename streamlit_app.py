import streamlit as st
from random import randint

def play_guessing_game():
    st.title("Guess the Number Game")
    st.write("Welcome to the Guess the Number game!")
    
    secret_number = randint(1, 50)
    attempts_left = 5
    
    st.write("I've picked a number between 1 and 50. You have 5 attempts to guess it!")
    
    while attempts_left > 0:
        guess = st.text_input("Enter your guess:")
        
        try:
            guess = int(guess)
        except ValueError:
            st.write("Invalid input! Please enter a valid number.")
            continue
        
        attempts_left -= 1
        
        if guess == secret_number:
            st.success(f"Congratulations! You guessed the secret number {secret_number} correctly!")
            break
        elif guess > secret_number:
            st.write(f"Try again! Your guess is too high. You have {attempts_left} attempts left.")
        else:
            st.write(f"Try again! Your guess is too low. You have {attempts_left} attempts left.")
    
    if attempts_left == 0:
        st.error(f"Game Over! The secret number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    play_guessing_game()

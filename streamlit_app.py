import streamlit as st
from random import randint

def play_guessing_game():
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = randint(1, 50)
        st.session_state.attempts_left = 5
        st.session_state.game_over = False

    st.title("Guess the Number Game")
    st.write("Welcome to the Guess the Number game!")
    
    if st.session_state.game_over:
        st.write("Game Over! Would you like to play again?")
        if st.button("Play Again"):
            st.session_state.secret_number = randint(1, 50)
            st.session_state.attempts_left = 5
            st.session_state.game_over = False
    else:
        st.write("I've picked a number between 1 and 50. You have 5 attempts to guess it!")
        
        while st.session_state.attempts_left > 0:
            guess = st.text_input("Enter your guess:")
            
            try:
                guess = int(guess)
            except ValueError:
                st.write("Invalid input! Please enter a valid number.")
                continue
            
            st.session_state.attempts_left -= 1
            
            if guess == st.session_state.secret_number:
                st.success(f"Congratulations! You guessed the secret number {st.session_state.secret_number} correctly!")
                st.session_state.game_over = True
                break
            elif guess > st.session_state.secret_number:
                st.write(f"Try again! Your guess is too high. You have {st.session_state.attempts_left} attempts left.")
            else:
                st.write(f"Try again! Your guess is too low. You have {st.session_state.attempts_left} attempts left.")
        
        if st.session_state.attempts_left == 0:
            st.error(f"Game Over! The secret number was {st.session_state.secret_number}. Better luck next time!")
            st.session_state.game_over = True

if __name__ == "__main__":
    play_guessing_game()

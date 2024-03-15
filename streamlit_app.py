import streamlit as st
import random

def guessing_game():
  """
  Function to run the guessing game logic
  """
  secret_number = random.randint(1, 50)
  attempts_left = 5
  game_over = False

  while attempts_left > 0 and not game_over:
    guess_str = st.text_input(f"Guess the number (between 1 and 50). You have {attempts_left} attempts left.")
    
    try:
      guess = int(guess_str)
    except ValueError:
      st.error("Invalid input! Please enter a valid number.")
      continue

    if guess == secret_number:
      st.success("Congratulations! You guessed the secret number correctly!")
      game_over = True
    elif guess > secret_number:
      attempts_left -= 1
      st.warning("Try again! Your guess is too high. You have {} attempts left.".format(attempts_left))
    else:
      attempts_left -= 1
      st.warning("Try again! Your guess is too low. You have {} attempts left.".format(attempts_left))

  if attempts_left == 0:
    st.error("Game Over! The secret number was {}. Better luck next time!".format(secret_number))

st.title("Guessing Game")
st.write("Try to guess the secret number between 1 and 50 in 5 attempts!")
guessing_game()

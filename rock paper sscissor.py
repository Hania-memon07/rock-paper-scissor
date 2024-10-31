import streamlit as st
import random

# Initialize game options
options = ["Rock", "Paper", "Scissors"]

# Title of the game
st.title("Rock-Paper-Scissors Game!")
st.write("Choose your option and see if you can beat the computer!")

# Take user input for the player's choice
user_choice = st.selectbox("Choose Rock, Paper, or Scissors:", options)

# Initialize or reset game state
if "result" not in st.session_state:
    st.session_state.result = ""

# Button to submit the choice and play the game
if st.button("Play"):
    # Generate computer's choice randomly
    computer_choice = random.choice(options)

    # Display choices
    st.write(f"You chose: {user_choice}")
    st.write(f"The computer chose: {computer_choice}")

    # Determine the winner and update result
    if user_choice == computer_choice:
        st.session_state.result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.session_state.result = "You win!"
    else:
        st.session_state.result = "Computer wins!"

    # Display the result
    st.write(st.session_state.result)

# Option to play again, which resets the result
if st.button("Play Again"):
    st.session_state.result = ""

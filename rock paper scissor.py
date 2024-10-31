import streamlit as st
import random

# Initialize game options
options = ["Rock", "Paper", "Scissors"]

# Title of the game
st.title("Rock-Paper-Scissors Game!")
st.write("Choose your option and see if you can beat the computer!")

# Take user input for the player's choice
user_choice = st.selectbox("Choose Rock, Paper, or Scissors:", options)

# Button to submit the choice
if st.button("Play"):
    # Generate computer's choice randomly
    computer_choice = random.choice(options)

   

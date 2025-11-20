import streamlit as st
import random

# -----------------------------
# INITIAL SETUP
# -----------------------------

WORDS = ["python", "apple", "banana", "orange", "hangman"]

# Initialize session state (runs only first time)
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = []
    st.session_state.wrong = 0
    st.session_state.game_over = False


# -----------------------------
# FUNCTIONS
# -----------------------------

def display_word():
    return " ".join([letter if letter in st.session_state.guessed else "_" 
                     for letter in st.session_state.word])

def guess_letter(letter):
    if st.session_state.game_over:
        return

    if letter not in st.session_state.guessed:
        st.session_state.guessed.append(letter)

        if letter not in st.session_state.word:
            st.session_state.wrong += 1

    # Check lose
    if st.session_state.wrong >= 6:
        st.session_state.game_over = True

    # Check win
    if "_" not in display_word():
        st.session_state.game_over = True


def reset_game():
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = []
    st.session_state.wrong = 0
    st.session_state.game_over = False


# -----------------------------
# UI LAYOUT
# -----------------------------

st.title("🎯 Hangman Game ")
st.subheader("Guess the hidden word!")

st.write("### Word:")
st.write(f"## {display_word()}")

st.write(f"**Wrong attempts:** {st.session_state.wrong} / 6")
st.write(f"**Guessed letters:** {', '.join(st.session_state.guessed)}")


# -----------------------------
# LETTER BUTTONS
# -----------------------------
st.write("### Choose a letter:")

cols = st.columns(9)
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i, letter in enumerate(alphabet):
    if cols[i % 9].button(letter.upper()):
        guess_letter(letter)


# -----------------------------
# GAME OVER LOGIC
# -----------------------------

if st.session_state.game_over:

    if "_" not in display_word():
        st.success("🎉 YOU WON!")
    else:
        st.error(f"❌ You Lost! The word was: **{st.session_state.word}**")

    if st.button("Play Again"):
        reset_game()


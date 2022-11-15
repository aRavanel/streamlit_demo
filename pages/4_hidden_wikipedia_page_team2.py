import streamlit as st

st.title("Guess the Secret Wikipedia Page!")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    text_input = st.text_input(
        "Write Your Guess 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled
    )

st.text("")
with open('constants/wikipedia.txt') as f:
    word = f.read()
    st.write(word)

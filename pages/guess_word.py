import streamlit as st

from src.model import Model
import src.global_data as DATA
from app import written_words, similarities

# ===================================================================
# UI definition
# ===================================================================
from dotenv import dotenv_values

env = dotenv_values(".env")

def calculate_similarity(word):
    return 666

def view(model):
    '''

    view (UI) of some dashboard

    '''
    st.set_page_config(layout='wide')

    st.title('Find the secret word!')

    textbox, button = st.columns(2)

    with textbox:
        word = st.text_input('Insert word here',label_visibility='collapsed')
    with button:
        if st.button('Enter'):
            similarity = calculate_similarity(word)
            written_words.append(word)
            similarities.append(similarity)

    col_words, col_similarities = st.columns(2)

    with col_words:
        for w in written_words:
            st.text(w)

    with col_similarities:
        for s in similarities:
            st.text(s)



view(DATA.globalmodel)





import streamlit as st

from src.model import Model
import src.global_data as DATA
from app import written_words, similarities
from src.global_data import w2v_model
from src.utils_nlp import calculate_temperature
# ===================================================================
# UI definition
# ===================================================================
from dotenv import dotenv_values

env = dotenv_values(".env")

wod = env['word_of_day']

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
            try:
                similarity = calculate_temperature(w2v_model, word, wod)
                written_words.append(word)
                similarities.append(similarity)
            except:
                st.write('Not ammitted word')

    col_words, col_similarities = st.columns(2)

    with col_words:
        for w in written_words:
            st.text(w)

    with col_similarities:
        for s in similarities:
            st.text(s)



view(DATA.globalmodel)





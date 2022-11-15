import streamlit as st

from src.model import Model
import src.global_data as DATA
from src.wikipedia_page import text
import re
# ===================================================================
# UI definition
# ===================================================================

def view(model):
    '''
    UI definition
    '''
    st.sidebar.markdown("# Page 2 ❄️")
    st.title('test page')
    st.subheader('this is a subheader')
    st.markdown("# Page 2 ❄️")
    title = st.text_input('Entre ton mot')
    result = st.button("Envoyer")
    if result:
        keep = [title, title.capitalize()]
        to_be_replaced = ["{", "}", "(", ")"]
        rx = '[' + re.escape(''.join(to_be_replaced)) + ']'
        text_clean = re.sub(rx, '', text)
        text_2 = re.sub(r'\b\w+\b', lambda w: w.group() if w.group() in keep else "❄️", text_clean)
        #words = text.replace("Une", "❄️")
        st.write(text_2)


# ===================================================================       
# Ui instanciation
# ===================================================================

view(DATA.globalmodel)





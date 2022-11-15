from dotenv import dotenv_values
import src.global_data as DATA
from src.model import Model
import streamlit as st

# UI
st.title('Find the secret word')
st.sidebar.markdown("# Homepage")
st.image("./resources/images/lefttab.png", width=400)


# assign some variable
DATA.globalmodel = Model()

# display some variable
env = dotenv_values(".env")
st.write("variable from .env file : " + env['some_variable'])

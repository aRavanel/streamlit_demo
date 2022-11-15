import streamlit as st

from src.model import Model
import src.global_data as DATA


st.write(" data input from page 2, globals : " + str(DATA.var_x))
st.write(" data input from page 2, global - data model : " + str(DATA.globalmodel.var_x))
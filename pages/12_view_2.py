import streamlit as st

from src.model import Model
import src.global_data as DATA

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
    st.write('hello this is a dirty page 2')
    
    display = ("male", "female")
    options = list(range(len(display)))
    # options = ['male','female']
    
    # drop down menu
    value = st.selectbox("gender", options, format_func=lambda x: display[x])
    
    # lets assign it to the global variables
    st.write("value of the dropdown : " + str(value))
    DATA.var_x = value
    model.var_x = value
    st.write("stored in globals : " + str(DATA.var_x))
    st.write("stored in data model : " + str(model.var_x))

# ===================================================================       
# Ui instanciation
# ===================================================================

view(DATA.globalmodel)





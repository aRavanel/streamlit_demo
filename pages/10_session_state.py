import streamlit as st

if 'somevar' not in st.session_state:
    st.session_state['somevar'] = 1
    
# v1 button
increment = st.button('Increment')
if increment:
    st.session_state['somevar']  += 1
    
#v2 button   
def increment_counter():
    st.session_state.somevar += 1    
increment2 = st.button('Incrementv2', on_click=increment_counter)
    

st.write(st.session_state.somevar)
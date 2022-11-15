import streamlit as st


original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
st.markdown(original_title, unsafe_allow_html=True)

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
st.markdown(new_title, unsafe_allow_html=True)

def style3(text):
    '''
    some style
    '''
    new_test = f'<p style="font-family:sans-serif; color:Red; font-size: 42px;">{text}</p>'
    return new_test

st.markdown(style3("babar"), unsafe_allow_html=True)

    

import streamlit as st
with open( "resources\styles\style_2.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    st.write(" hello")
    
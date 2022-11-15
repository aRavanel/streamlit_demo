import streamlit as st

# UI
st.title('WELCOME TO THE ART UI CODING THING')
#st.markdown("# title 1")
#st.markdown("## title 1.1")
#st.markdown("# title 2")
#st.write('lets write some streamlit')
st.sidebar.markdown("# Homepage")

tab1, tab2, tab3 = st.tabs(["Hidden word game", "Wikipedia game", "Leo"])

with tab1:
   st.header("Hidden word game")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=500)

with tab2:
   st.header("Wikipedia game")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=500)

with tab3:
   st.header("A Leo")
   st.image("https://media.licdn.com/dms/image/C4D03AQFJjJ9syd_Xdg/profile-displayphoto-shrink_800_800/0/1598000714687?e=1672876800&v=beta&t=alZjhawrKmb1kqZH9m36-rVOgKNS-QAy1jCLaISkggU", width=200)

# assign some variable
from src.model import Model
import src.global_data as DATA
DATA.globalmodel = Model()

# display some variable
from dotenv import dotenv_values
env = dotenv_values(".env") 
st.write("variable from .env file : " + env['some_variable'] )


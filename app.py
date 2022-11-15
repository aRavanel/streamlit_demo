import streamlit as st
<<<<<<< HEAD
import datetime
import src.global_data as DATA

=======
from src.utils_nlp import load_model
>>>>>>> 1f0275e6ac3124d4b3ed3267483471a44921c0a3
written_words = []
similarities = []

# Loading model in memory
w2v_model = load_model()

# UI
st.title('WELCOME TO THE ART UI CODING THING')
#st.markdown("# title 1")
#st.markdown("## title 1.1")
#st.markdown("# title 2")
#st.write('lets write some streamlit')
st.sidebar.markdown("# Homepage")

tab1, tab2, tab3 = st.tabs(["Hidden word game", "Wikipedia game", "Leo"])

with tab1:

    st.title('Counter Example')

    if 'count' not in st.session_state:
        st.session_state.count = 0
        st.session_state.count_history = []
        st.session_state.last_updated = datetime.time(0,0)

    def update_counter():
        st.session_state.count += st.session_state.increment_value
        st.session_state.count_history.append(st.session_state.increment_value)
        st.session_state.last_updated = st.session_state.update_time

    with st.form(key='my_form'):
        st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
        st.number_input('Enter a value', value=0, step=1, key='increment_value')
        submit = st.form_submit_button(label='Update', on_click=update_counter)

    st.write('Current Count = ', st.session_state.count)
    st.write('Last Updated = ', st.session_state.last_updated)

    st.write('Past vals')
    for i in st.session_state.count_history:
        st.write(i)

    st.session_state.count_history
    DATA.global_counter = st.session_state.count_history

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


import streamlit as st
tab1, tab2, tab3 , tab4= st.tabs(["Cat", "Dog", "Owl", 'Leo'])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
with tab4:
   st.header("A Leo")
   st.image("https://media.licdn.com/dms/image/C4D03AQFJjJ9syd_Xdg/profile-displayphoto-shrink_800_800/0/1598000714687?e=1672876800&v=beta&t=alZjhawrKmb1kqZH9m36-rVOgKNS-QAy1jCLaISkggU", width=200)
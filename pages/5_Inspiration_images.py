import streamlit as st
from PIL import Image

im = Image.open('./resources/images/cool_group.png')
st.image(im, caption='😝sorry Eoin...')
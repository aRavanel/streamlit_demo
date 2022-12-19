import streamlit as st
import cv2 as cv2
from PIL import Image
from datetime import date
from datetime import datetime
import numpy as np
import random

from src.video_utils_2 import *

import streamlit as st
#CameraThread is a sub-class of threading.Thread

@st.cache(allow_output_mutation=True)
def get_or_create_camera_thread():
    for th in threading.enumerate(): # Returns a list of all thread objects that are currently active.
        if th.name == 'CameraThread':
            th.stop()
            th.join() # The join() waits for threads to terminate.
    cw = CameraThread(name='CameraThread')
    cw.start() # The start() method starts a thread by calling the run method.
    return cw


camera = get_or_create_camera_thread()

# Create UI
st_frame = st.empty()

if 'explain_button' not in st.session_state: st.session_state['explain_button'] = 'None'
def button_action():
    st.session_state['explain_button']  = str(datetime.now())
st.button('take picture', on_click=button_action)
st.write(st.session_state['explain_button'])
        
while True:
    frame = camera.read()
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    st_frame.image(frame_RGB)
    


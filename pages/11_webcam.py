import streamlit as st
import cv2 as cv2
from PIL import Image
from datetime import date
from datetime import datetime
import numpy as np
import random



# initialize state
if 'explain_button' not in st.session_state: st.session_state['explain_button'] = 'None'
if 'state_cam' not in st.session_state: st.session_state['state_cam'] = 'None'
if 'explain_image' not in st.session_state: st.session_state['explain_image'] = 'None'
if 'picture' not in st.session_state:
    st.session_state['picture'] = Image.open('./resources/images/placeholder.png')


# v1 
# create an object of video capture. 0 is the index of the camera (first one)
# camera = cv2.VideoCapture(0)


# =====================================
# UI 
# =====================================

st.title("Webcam Live Feed")

col_1, col_2, col_3 = st.columns((2,1,2))
 
# column 1
# ---------
with col_1:
    # frame for image
    FRAME_WINDOW = st.image([])
    
    # new code
    import src.video_utils as video_utils
    available_cameras = {'Camera 1': 0, 'Camera 2': 1, 'Camera 3': 2}
    video_source = available_cameras['Camera 1']
    video_thread = video_utils.WebcamVideoStream(video_source)
    img_placeholder = st.empty()
    
    # checkbox to launch
    def callback_checkbox_run_webcam():
        '''
        activate when on run
        '''
        previousRun = bool(run) # value of run before changing
        newRun = not previousRun
        if newRun: # while checkbox display
            st.session_state['state_cam'] = 'state_cam_ON'

            # while run:
            # _, frame = camera.read()
            # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # st.session_state['curr_image'] = frame_rgb
            # FRAME_WINDOW.image(frame_rgb)
            
            # new code
            video_thread.start()
            
        
        else:
            st.session_state['state_cam'] = 'state_cam_OFF'
            
            # new code
            video_thread.stop()
        
    run = st.checkbox('Run', key='checkbox_run_webcam', on_change=callback_checkbox_run_webcam)
    
    if run:
        while not video_thread.stopped():
            # Camera detection loop
            frame = video_thread.read()
            if frame is None:
                print("Frame stream interrupted")
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Change color gammut to feed the frame into the network
            img_placeholder.image(frame)  # Display the image with the detections in the Streamlit app
    # 
    
    

    # some info
    st.write("run boolean : " + str(run))
    st.write(st.session_state['state_cam'])

    # Button take picture 
    def button_action():
        st.session_state['explain_button']  = str(datetime.now())
        # try:
        #     st.session_state['picture']  = frame_rgb
        # except:
        #     st.session_state['picture']  = None
        
        # save an image
        try:
            im_pil = Image.open('./resources/images/placeholder.png')
            im_pil = im_pil.rotate(random.randint(1,45))
            im_pil.save('./resources/images/placeholder2.png')
        
        except:
            im_pil = Image.open('./resources/images/placeholder.png')
            im_pil = im_pil.rotate(random.randint(1,45))
            im_pil.save('./resources/images/placeholder2.png')
        
        st.session_state['picture'] = Image.open('./resources/images/placeholder2.png')
            

    st.button('take picture', on_click=button_action)
    st.write(st.session_state['explain_button'])
    
# column 3
# --------
with col_3:
    if 'picture' not in st.session_state:
        st.session_state['explain_image'] = 'explain_image not defined'
    else:
        st.session_state['explain_image'] = 'lets use frame : ' + st.session_state['explain_button']
        
    st.write(st.session_state['explain_image'])     
    st.image(st.session_state['picture'], caption='screenshot')
    # st.write("sssssssssssssssssss")
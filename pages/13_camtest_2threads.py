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

# define a thread that is going to do the update
# instead of  while loop that will block code after
import threading
from queue import Queue # to send message to the thread

threadLock = threading.Lock()
threads = []

class myThread (threading.Thread):
    def __init__(self, threadID, name, queue, camera, st_frame):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queue = queue
        
        self.camera = camera
        self.st_frame = st_frame
        
    def run(self):
        print ("Starting " + self.name)
        
        threadLock.acquire()  # Get lock to synchronize threads
        
        while True:
            print('in true loop')
            try:
                val = self.queue.get_nowait() # get : waits for a value to take from queue. get_nowait() doesnt wait
                print('try val : ', val)
            except:
                val = 0
                print('except queu')
            
            # do something
            
            # exit if value put in queue
            if val == 1:
                break
            
            
        threadLock.release()  # Free lock to release next thread


q = Queue() # create FIFO queue
thread1 = myThread(1, "Thread-1", q, camera, st_frame)# Create new threads
thread1.start()# Start new Threads

import time

thread1.queue.put(4)
time.sleep(1)
thread1.queue.put(3)
time.sleep(1)
thread1.queue.put(2)
time.sleep(1)
thread1.queue.put(1) # message to end it
 
# Add threads to thread list
threads.append(thread1)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")

# while True:
#     frame = camera.read()
#     frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     st_frame.image(frame_RGB)
    


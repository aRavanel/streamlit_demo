import streamlit as st
import pandas as pd
import plotly.express as px
from src.model import Model

# ===================================================================
# UI definition
# ===================================================================
def view(model):
    '''
    view (UI) of some dashboard
    '''
    st.set_page_config(layout = 'wide')
    st.title('🎈 Cemantix app')
    st.header(model.header)
    
    # create thre columns with relative weidths
    commentaryCol, spaceCol, chartCol = st.columns((2,1,6))

    # Fill left column (commentary)
    with commentaryCol:
        # using a container (not mandatory)
        c = st.container()
        c.write('')
        c.write('')
        c.write(model.description)
        
        # Year Slider
        st.write('')
        st.write('')
        year = st.slider(model.sliderCaption,
                         model.yearStart, model.yearEnd, 
                         model.yearStart, model.yearStep)
        
        model.x = year
        st.write('data model is being updated with slider :'+ str(model.x) )

    # Fill right column (chart)
    with chartCol:
        st.plotly_chart(model.chart(year), use_container_width = True)
 
# ===================================================================       
# Ui instanciation
# ===================================================================

view(Model())
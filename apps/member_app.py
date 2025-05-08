import datetime
import io
from hydralit import HydraHeadApp
import astropy.units as u
import pandas as pd
import streamlit as st
from astropy.coordinates import SkyCoord
from sunpy.coordinates import frames
import hydralit_components as hc


class MemberApp(HydraHeadApp):

    def __init__(self, title = 'Member', **kwargs):
        # self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        # Ideal_title = '<p style="font-family:; color:#071947; font-size: 25px; ">Advisor and member of project</p>'
        # st.markdown(Ideal_title, unsafe_allow_html=True)
        

        # footer
        # st.markdown("""---""")
        st.image('resources/memb.png',use_column_width=400, clamp=False, channels="RGB", output_format="auto")
        
    

import streamlit as st
import hydralit_components as hc
import codecs
from hydralit import HydraHeadApp
import streamlit.components.v1 as stc 

class DashbApp(HydraHeadApp):

    def __init__(self, title = 'Dashboard', delay=0, **kwargs):
        # self.__dict__.update(kwargs)
        self.title = title
        # self.delay = delay

    def run(self):
        st.title("Dashboard for data set")
                #### import html ####
        
        def st_webpage(page_html,width=2000,height=2000):
            page_file = codecs.open(page_html,'r')
            page =page_file.read()
            stc.html(page,width=width, height=height , scrolling = False)
        st_webpage('apps/powerBI.html')
        
        
        
        

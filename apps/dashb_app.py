import streamlit as st
import hydralit_components as hc
import codecs
from hydralit import HydraHeadApp
import streamlit.components.v1 as stc 
import base64
import pdfplumber

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])



if uploaded is not None:
    if st.button("👁️ แสดงเนื้อหา PDF"):
        text = extract_text_from_pdf(uploaded)
        st.text_area("📄 เนื้อหา PDF", text, height=600)
class DashbApp(HydraHeadApp):

    def __init__(self, title = 'Dashboard', delay=0, **kwargs):
        # self.__dict__.update(kwargs)
        self.title = title
        # self.delay = delay
    
    def run(self):
        st.title("Dashboard for data set")
                #### import html ####
        
        def st_webpage(page_html,width=1190,height=600):
            page_file = codecs.open(page_html,'r')
            page =page_file.read()
            stc.html(page,width=width, height=height , scrolling = False)
        st_webpage('apps/powerBI.html')
        uploaded = st.file_uploader("📎 Upload PDF", type="pdf")
        
        
        

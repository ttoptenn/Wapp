import streamlit as st
import hydralit_components as hc
import codecs
from hydralit import HydraHeadApp
import streamlit.components.v1 as stc 
import base64
from pathlib import Path

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
        
        with tab2:
            pdf_path = Path("apps/Handbook for dashboard.pdf")
        
            if pdf_path.exists():
                with open(pdf_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
                pdf_display = f"""
                    <iframe src='data:application/pdf;base64,{base64_pdf}' width='800' height='1000' type='application/pdf'></iframe>
                """
                st.markdown("### 📑 Handbook Preview")
                st.markdown(pdf_display, unsafe_allow_html=True)
        
                with open(pdf_path, "rb") as f:
                    st.download_button("📥 ดาวน์โหลด Handbook", f, file_name="Handbook for dashboard.pdf")
            else:
                st.warning("ไม่พบไฟล์ Handbook for dashboard.pdf")

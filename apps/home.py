import os
import apps
import streamlit as st
import json
import requests
# from apps import pred_app
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from hydralit import HydraHeadApp
#-----------------------------------------------------------------------------------------------------------------------------

MENU_LAYOUT = [1,1,1,7,2]
class HomeApp(HydraHeadApp):


    def __init__(self, title = 'home', **kwargs):
        # self.__dict__.update(kwargs)
        self.title = title

    def run(self):

        try:    
            #### sticker image ####
            def load_lottiefile(filepath: str):
                with open (filepath,"r") as f:
                    return json.load(f)

            # json animation ---------------------------------------------------------------------
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()  
            
            # lottie2_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_vckswclv.json.svg")
            # st_lottie(lottie2_coding, height=400,  key="codving")
            # lottie2_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_nw19osms.json")
            # st_lottie(lottie2_coding, height=400,  key="coding")
            # lottie2_codingg = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_pk5mpw6j.json")
            # st_lottie(lottie2_codingg, height=400,  key="codingg")
            lottie2_codingss = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_vckswclv.json")
            st_lottie(lottie2_codingss, height=230,  key="codvings")
            
            with st.container():
                left_column1,left_column2,left_column3, right_column,right_column2 = st.columns((0.5,2.5,6,2,0.5))
                with left_column3:                  
                    st.title(" 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠Web Application for  󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠Antimicrobial Peptide Prediction ")
                    # st.subheader("เว็บแอปพลิเคชันสำหรับการทำนายเพปไทด์ต้านจุลชีพ")
                    Ideal_title = '<p style="font-family:; color:#31333F; font-size: 28px; ">Web Application to test the antimicrobial peptide activity against bacteria.</p>'
                    # st.markdown(Ideal_title, unsafe_allow_html=True)
            # st.image('resources/waapp.png',width=1430,use_column_width=None, clamp=False, channels="RGB")
            
               
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, we humbly request you try again.')
            st.error('Error details: {}'.format(e))



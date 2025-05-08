# .............................................................................................................................
from hydralit import HydraApp
import hydralit_components as hc
import apps
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import streamlit.components.v1 as stc
import json
import pandas as pd
import numpy as np
# -------------------------------------------------------------------------------------------------------------------------------------

#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='antimicrobial peptide',page_icon=":pill:",layout='wide',initial_sidebar_state='auto',)

if __name__ == '__main__':
    with open('style2.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        #---ONLY HERE TO SHOW OPTIONS WITH HYDRALIT - NOT REQUIRED, use Hydralit constructor parameters.
        st.write("##")
        hide_st = ('Hide Streamlit Markers',True)
        over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#1F3D7C','txc_active':'#F36C23','option_active':'#FFFFFF'}
        #this is the host application, we add children to it and that's it!
        app = HydraApp(
            title='Secure Hydralit Data Explorer',
            favicon=":pill:",
            hide_streamlit_markers=hide_st,
            #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
            use_banner_images=["resources/pig0.png",None,{'header':"<h1 style='text-align:center;padding: 0px 0px;color:F36C23;font-size:175%;'>WAAPP: Web Application for Antimicrobial Peptide Prediction</h1>"},None,"./resources/lock.png"], 
            banner_spacing=[6,15,60,15,4.5],
            navbar_theme=over_theme
        )

        with open('style2.css') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        #Home button will be in the middle of the nav list now
        app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)

        #add all application classes
        app.add_app("Predict your peptide", icon="🔍", app=apps.PredictApp(title="Predict your peptide"))
        app.add_app("How to use web application", icon="❓", app=apps.HowtoApp(title="How to use web application"))
        app.add_app("Dashboard", icon="far fa-chart-bar", app=apps.DashbApp(title="Dashboard"))
        app.add_app("Intro", icon="🏆", app=apps.IntroApp(title="About us"))
        app.add_app("Member", icon="👩‍🏫", app=apps.MemberApp(title="Member"))
        app.add_app("Contact us", icon="📧", app=apps.ContactUsAPP(title="Contact us"))

        #check access
        username = app.check_access()

        # def st_webpage(page_html,width=1370,height=1550):
        #     page_file = codecs.open(page_html,'r')
        #     page =page_file.read()
        #     stc.html(page,width=width, height=height , scrolling = False)

        # If the menu is cluttered, just rearrange it into sections!
        # completely optional
        if username:
            complex_nav = {
                'Home': ['Home'],
                'Predict your peptide': ["Predict your peptide"],
                'How to WebApp': ["How to use web application"],
                'Dashboard': ['Dashboard'],
                '🕮 About us': ['Intro',"Member"],
                'Contact us': ['Contact us']
            }
    
        else:
            complex_nav = {
                'Home': ['Home'],
            }

        #and finally just the entire app and all the children.
        app.run(complex_nav)


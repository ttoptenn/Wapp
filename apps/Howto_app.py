import streamlit as st
from hydralit import HydraHeadApp

# -------------------------------------------------------------------------------------------------------------------------------------
class HowtoApp(HydraHeadApp):

    def __init__(self, title = 'How to use web application', **kwargs):
        # self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        Ideal_hp = '<div align="center"><p style="font-family:; color:#000000; font-size: 35px; background-color: #C2DFFF; border-radius: 5px;">How to use</p>'
        st.markdown(Ideal_hp, unsafe_allow_html=True)
        Ideal_1 = '<div align="center"><p style="font-family:; color:#000000; font-size: 20px; background-color: #C2DFFF; border-radius: 5px;">Home page</p>'
        st.markdown(Ideal_1, unsafe_allow_html=True)
        st.image('resources/webp1.png', width = 1450)
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        Ideal_2 = '<div align="center"><p style="font-family:; color:#000000; font-size: 20px; background-color: #C2DFFF; border-radius: 5px;">Prediction page</p>'
        st.markdown(Ideal_2, unsafe_allow_html=True)
        st.image('resources/webp2.png', width = 1450)
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        Ideal_3 = '<div align="center"><p style="font-family:; color:#000000; font-size: 20px; background-color: #C2DFFF; border-radius: 5px;">Dashboard page</p>'
        st.markdown(Ideal_3, unsafe_allow_html=True)
        st.image('resources/webp3.png', width = 1450)
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')
        Ideal_4 = '<div align="center"><p style="font-family:; color:#000000; font-size: 20px; background-color: #C2DFFF; border-radius: 5px;">Contact us page</p>'
        st.markdown(Ideal_4, unsafe_allow_html=True)
        st.image('resources/webp4.png', width = 1450)
        st.write('##')
        st.write('##')
        st.write('##')
        st.write('##')

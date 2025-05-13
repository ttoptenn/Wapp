import streamlit as st
from hydralit import HydraHeadApp
from streamlit_lottie import st_lottie
import json
import requests
# from hydralit_components import CookieManager


class ContactUsApp(HydraHeadApp):

    def __init__(self, title = 'Contact us', delay=0, **kwargs):
        # self.__dict__.update(kwargs)
        self.title = title
        # self.delay = delay

    def run(self):

        try:   
            tss1,tss2,dsss,tss3,tss4 = st.columns((0.6,3,0.9,5,0.6))
            with tss2:
                def load_lottieurl(url: str):
                    r = requests.get(url)
                    if r.status_code != 200:
                        return None
                    return r.json()
                lottie2_codingsdd = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_isbiybfh.json")
                st_lottie(lottie2_codingsdd, height=300,  key="codvingzq") 
            with tss3:
                st.header(":mailbox: Contact Us")
                # Instead of form, just display the email address
                st.write("For any inquiries, please contact us at:")
                st.write("[woranich.hin@cra.ac.th](mailto:woranich.hin@cra.ac.th)")
                st.write("[peerut.chi@cra.ac.th](mailto:peerut.chi@cra.ac.th)")

                def local_css(file_name):
                    with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                local_css("style2.css")
            
            st.write("##")
            st.markdown("""---""")
        except Exception as e:
            st.error(f"An error occurred: {e}")
                
            #st.header("Contact Us ☎️")
            

            #t1,t2,aaw,ds,ssa,t3,tn4= st.columns((0.5,5,0.2,0.5,0.01,5,3))
            #t1.write("##")
            #t1.image('resources/pig2.png', width = 45)
            # t2.write("ภาควิชาวิศวกรรมคอมพิวเตอร์")
            #with t2:
                #st.write("##")
                #Ideal_d1 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;"> 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠Bachelor of Computer Engineering.</p>'
                #t2.markdown(Ideal_d1, unsafe_allow_html=True)
                # t2.write("มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี")
                #Ideal_d2 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;"> 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠King Mongkut’s University of Technology Thonburi</p>'
                #t2.markdown(Ideal_d2, unsafe_allow_html=True)
                # t3.write("ชั้น 10-11, อาคารวิศววัฒนะ, มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี ")
                # Ideal_d3 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">ชั้น 10-11, อาคารวิศววัฒนะ, มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี</p>'
                # t3.markdown(Ideal_d3, unsafe_allow_html=True)
                # t3.write("126 ถนนประชาอุทิศ แขวงบางมด เขตทุ่งครุ กรุงเทพฯ 10140 ")
                #Ideal_d4 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;"> 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠126 Pracha Uthit Rd, Bang Mot, Thung Khru, Bangkok 10140</p>'
                #t2.markdown(Ideal_d4, unsafe_allow_html=True)
                # t4.write("(+66) 0-2470-9388")
                #Ideal_d5 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;"> 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠 󠀠📞 Phone: (+66)-2470-9388</p>'
                #t2.markdown(Ideal_d5, unsafe_allow_html=True)
                # t4.write("E-mail: nongyao.jam@mail.kmutt.ac.th")
                # Ideal_d6 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">E-mail: nongyao.jam@mail.kmutt.ac.th</p>'
                # t4.markdown(Ideal_d6, unsafe_allow_html=True)
                #col_header_text,col_header_logo_right,col_header_logo_right_far = st.columns([2,2,1])

                #col_header_logo_right_far.image(os.path.join(".","resources","hydra.png"),width=100,)
                

            # t3.write("##")
            #ds.write("##")
            #ds.image('resources/pig1.png', width = 40)
            # t2.write("วิทยาลัยแพทยศาสตร์ศรีสวางควัฒน")
            #with t3:
                #st.write("##")
                #Ideal_d7 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">Srisavangavadhana College of Medicine,</p>'
                #st.markdown(Ideal_d7, unsafe_allow_html=True)
                # t2.write("ราชวิทยาลัยจุฬาภรณ์")
                #Ideal_d8 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">Chulabhorn Royal Academy</p>'
                #st.markdown(Ideal_d8, unsafe_allow_html=True)
                # t3.write("906 ถ.กำแพงเพชร 6 แขวงตลาดบางเขน เขตหลักสี่ กรุงเทพมหานคร 10210")
                #Ideal_d9 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">906 Kamphaeng Phet 6 Road, Talat Bang Khen, Lak Si, Bangkok 10210</p>'
                #st.markdown(Ideal_d9, unsafe_allow_html=True)
                # t4.write("สายด่วน รจภ. 1118, 0-2576-6718")
                #Ideal_d10 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">📞 Phone: (+66)-2576-6718</p>'
                #st.markdown(Ideal_d10, unsafe_allow_html=True)
                
            #with tn4:
                #lottie2_cod = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_sj0skmmg.json")
                #st_lottie(lottie2_cod, height=200,  key="codvzq") 
            
            #ssm1,ssm2,ssm3,ssm4,ssm5= st.columns((0.1,5,0.1,5,2))
            #if ssm2.button('This will open a KMUTT Website'):
                    #self.do_redirect("https://www.kmutt.ac.th/")
            # st.write("##")
            #if ssm4.button('This will open a CHULABHORN ROYAL ACADEMY Website'):
                    #self.do_redirect("https://pscm.cra.ac.th/")
            # st.write("##")
      
        #except Exception as e:
            #st.image("./resources/failure.png",width=100,)
            #st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            #st.error('Error details: {}'.format(e))

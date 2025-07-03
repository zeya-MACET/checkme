import streamlit as st
from streamlit_option_menu import option_menu
import about, watch, home, islamic, family

st.set_page_config(
    page_title="Zeya on Net",
    
    #Title
    #st.title("welcome to My HOME Page Website in Python")
    #Header
    #st.header("Its a Website for Test Purpose only")

)

class MultiApp:

    def  __init__(self):
        self.app = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function          
           
        })
        
    def run():  
        
        #st.title(" Welcome to Multiple Page Website")
        #with st.sidebar:
        #with st.sidebar:
        app = option_menu(
                menu_title=None,#('STAR is blinking  '),
                options=['Home','Watch','Islamic','Family','About'],
                #icons=['house-fill','watch','trophy-fill','phone','trophy-fill','info-circle-fill'],
                menu_icon='chat-txt-fill',
                default_index=0,
                orientation="horizontal",
                styles={
                "container": {"padding": "5!important","background-color":'yellow'},
                #"icon": {"color": "green", "font-size": "23px"},
                #"nav-link": {"color":"black","font-size":  "20px", "text-align": "left", "margin":"0px"},
                "na-link-selected": {"background-color": "#02ab21"},}
               )
            
       
        if app== 'Home':
            home.app()
        if app== 'Watch':
            watch.app()
        if app== 'Islamic':
            islamic.app()
        if app== 'Family':
            family.app()
        if app== 'About':
             about.app()
        
        #################################################################################################################
  
        #################################################################################################################




    run()

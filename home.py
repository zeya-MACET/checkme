import streamlit as st
import datetime

def app():
    #Title
    #st.title("welcome to My :green[HOME] Page Website in Python]",)
    
    #st.image(image, channels="BGR")
    #st.title("_Streamlit_ is :blue[cool] :sunglasses:")
    #st.title(":blue[Streamlit WEB Page_ is much]")
    #st.title(":red[Excelent-Streamlit WEB Page_ is much]")
    #Header
    #st.header(":green[Home Page]")

    st.button("Website is still in  Development Period.................................")

    ###########################
    
    import datetime
   
    #st.date_input(':red[Today Date is]',datetime.datetime.now())
    
    st.write(f":red[] {datetime.datetime.now()}")

    #st.write(f":red[Current Time is:] {datetime.datetime.now()}")


    from datetime import datetime

    #######################Display Only Time##############################

        
    #######################End of Time Display############################

    # Get the current day
    current_day = datetime.now().strftime("%A")

    # Display the current day on the Streamlit page
    #st.title("Current Day Display")
    #st.write(f":green[Today is:] {current_day}")

    # Get the current month name
    current_month = datetime.now().strftime("%B")

    # Display the month name on the Streamlit page
    #st.title("Current Month")
    #st.write(f"The current month is: {current_month}")

    # Get the current year
    current_year = datetime.now().year

    # Display the current year on the Streamlit page
    #st.write(f"The current year is {current_year}")

    ####################Test ##########################
    import datetime
    st.write(f":green[] :blue[{current_day} {current_month} {current_year}]")#,st.date_input(':blue[]',datetime.datetime.now())

    ####################Test End ######################


    from PIL import Image
    img = Image.open('CDBA.jpg')
    st.image(img,caption='my home page')


    ############################
    #st.image(E:\My Development\Python\Website in Python\solar.png)
    #subheader
    #st.subheader("Streamlit Tutorial")
    #text
    #st.text(''' Helloe Everyone Welcome to my Python Station Streamlit 
            #Hope you will check it......''')
    #write
    #st.write('Please Subscribe my Python Channel')
    #Image and Caption
    #from PIL import Image
    #img = Image.open('SolarSystem.png')
    #st.image(img,caption='Solar System')
    #Colourful text
    #success
    st.success('success')
    #balloowns
    #st.balloons()
    st.balloons()



 


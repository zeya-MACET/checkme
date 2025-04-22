import streamlit as st

def app():
    #Title
    #st.title("welcome to My :green[Posts] Page Website in Python")
    #Header
    st.header(":green[My Family Page]")

    #st.button("Website Development is in Progress")
    #st.image(E:\My Development\Python\Website in Python\solar.png)
    #subheader
    #st.subheader("Streamlit Tutorial")
    #text
    #st.text(''' Helloe Everyone Welcome to my Python Station Streamlit 
            #Hope you will check it......''')
    #write
    #st.write('Please Subscribe my Python Channel')
    #Image and Caption
    from PIL import Image
    img = Image.open('family.png')
    st.image(img,caption='My Family Tree')
    #Colourful text
    #success
    st.success('success')
    
    #balloowns
    st.balloons()



 


import streamlit as st

def app():
    #Title
    #st.title("welcome to My :red[ABOUT] Page Website in Python")
    #Header
    st.header(":green[About Me]")

    #st.button("Website Development is in Progress")
    #st.image(E:\My Development\Python\Website in Python\solar.png)
    #subheader
    st.subheader("Mohammad Zeyaul Islam Siddiqui")

    myemailid=("Email: zeyaulislamp@gmail.com")

    st.write(myemailid)
    #text
    #st.text(''' Email:  zeyaulislamp@gmail.com 
            #Hope you will check it......''')
    #write
    #st.write('Please Subscribe my Python Channel')
    #Image and Caption
    from PIL import Image
    img = Image.open('aboutme.png')
    st.image(img)#,caption='Solar System')
    #st.image(img,caption='Solar System')
    #Colourful text
    #success
    st.success('success')
   
    #balloowns
    st.balloons()



 


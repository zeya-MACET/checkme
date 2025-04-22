import streamlit as st

def app():
    #Title
    #st.title("welcome to My :violet[Trending] Page Website in Python")
    #Header
    st.header(":violet[My Islamic page]")

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
    img = Image.open('Islamic.png')
    st.image(img,caption='Islamic Holy Places')
    #Colourful text
    #success
    st.text("Makkah Information")
    makkah=("https://en.wikipedia.org/wiki/Mecca")
    st.write(makkah)

    st.text("Madinah Information")
    madinah=("https://en.wikipedia.org/wiki/Medina")
    st.write(madinah)

    st.text("Masjeda Al Nabwi Madinah Information")
    madinahm=("https://simple.wikipedia.org/wiki/Al-Masjid_an-Nabawi")
    st.write(madinahm)

    st.text("Masjeda Al Haram Makkah Information")
    makkahm=("https://en.wikipedia.org/wiki/Masjid_al-Haram")
    st.write(makkahm)

    st.text("Masjeda Al Aksa Information")
    aksa=("https://en.wikipedia.org/wiki/Al-Aqsa_Mosque")
    st.write(aksa)


    st.success('success')
    
    
    #balloowns
    st.balloons()



 


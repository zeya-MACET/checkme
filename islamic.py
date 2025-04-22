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

    st.text("Makkah Masjeda Al Haram Live 1 to 3 ")
    makkahlive1=("https://www.youtube.com/watch?v=eJNWHKld5E8")
    makkahlive2=("https://www.youtube.com/watch?v=PPVvoWbReMI")
    makkahlive3=("https://www.youtube.com/watch?v=bNY8a2BB5Gc")
    st.write(makkahlive1)
    st.write(makkahlive2)
    st.write(makkahlive3)
    st.text("Madinah Information")
    madinah=("https://en.wikipedia.org/wiki/Medina")
    st.write(madinah)
    st.text("Madinah Masjeda Al Nabwi Live 1 to 3 ")
    madinahlive1=("https://www.youtube.com/watch?v=rHWSRMcGGBQ")
    madinahlive2=("https://www.youtube.com/watch?v=yWw0DWJQVtU")
    madinahlive3=("https://www.youtube.com/watch?v=naaOMgZbIHQ")
    st.write(madinahlive1)
    st.write(madinahlive2)
    st.write(madinahlive3)

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



 


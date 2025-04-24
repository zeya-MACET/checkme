import streamlit as st

def app():
    
    st.header(":violet[My Islamic page]")

    
    from PIL import Image
    img = Image.open('Islamic.png')
    st.image(img,caption='Islamic Holy Places')
  
    st.write("[Makkah](https://en.wikipedia.org/wiki/Mecca)")
    st.write("[Madinah](https://en.wikipedia.org/wiki/Medina)")
    st.write("[Masjeda Al Nabwi Madinah ](https://simple.wikipedia.org/wiki/Al-Masjid_an-Nabawi)")
    st.write("[Masjid al-Aqsa (Bayt al-Maqdis) Jerusalem](https://en.wikipedia.org/wiki/Al-Aqsa_Mosque)")
    st.write("[Masjeda Al Haram Makkah](https://en.wikipedia.org/wiki/Masjid_al-Haram)")    
    st.write("[Makkah Masjeda Al Haram Live 1](https://www.youtube.com/watch?v=eJNWHKld5E8)")
    st.write("[Makkah Masjeda Al Haram Live 2](https://www.youtube.com/watch?v=PPVvoWbReMI)")
    st.write("[Makkah Masjeda Al Haram Live 3](https://www.youtube.com/watch?v=bNY8a2BB5Gc)")
    st.write("[Madinah Masjeda Al Nabwi Live 1](https://www.youtube.com/watch?v=rHWSRMcGGBQ)")
    st.write("[Madinah Masjeda Al Nabwi Live 2](https://www.youtube.com/watch?v=yWw0DWJQVtU)")
    st.write("[Madinah Masjeda Al Nabwi Live 3](https://www.youtube.com/watch?v=naaOMgZbIHQ)")
    

    st.success('success')
    
    
    #balloowns
    st.balloons()



 


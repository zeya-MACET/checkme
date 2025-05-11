import streamlit as st


def app():
    
        
    from PIL import Image
    img = Image.open('Islamic.png')
    st.image(img,caption='Islamic Holy Places')

    
    st.markdown("<h1 style='text-align: center; color: green;'>Five Pillars of Islam</h1>", unsafe_allow_html=True)
    #st.markdown("This is black and :red[this is red!]")

    st.write("[1: Shahada(Faith)الشَهادة](https://en.wikipedia.org/wiki/Shahada)")
    st.image("Shadahm.png", caption="(ٱلشَّهَادَةُ)")
    st.markdown("<h2 style='text-align: center; color: green;'>Six Kalma چھ کلمے </h2>", unsafe_allow_html=True)
    

        # Create columns for horizontal button arrangement
    col1, col2, col3, col4, col5, col6 = st.columns(6)

        # Add buttons to each column
    with col1:
                if st.button("kalma No 1 پہلا کلمہ"):
                    #st.write("Button 11 clicked!")
                    #st.write("[Makkah](https://en.wikipedia.org/wiki/Mecca)")
                    #st.write("[Makkah](Faith.htm)")---Not working
                    #display_html('Faith.htm')
                    st.image("Kalma-1.jpg", caption="Kalma 1")
                    #st.image("namaz-ka-lafz-ba-lafz-urdu-tarjuma.pdf", caption="Kalma 1")                    

    with col2:
                if st.button("kalma No 2 دوسرا کلمہ"):
                    #st.write("Button 22 clicked!")
                    st.image("Kalma-2.jpg", caption="Kalma 2 دوسرا کلمہ")

    with col3:
                if st.button("kalma No 3 تیسرا کلمہ"):
                    #st.write("Button 33 clicked!")
                    st.image("Kalma-3.jpg", caption="Kalma 3 تیسرا کلمہ")
    with col4:
                if st.button("kalma No 4 چوتھا کلمہ"):
                    #st.write("Button 44 clicked!")
                    st.image("Kalma-4.jpg", caption="Kalma 4 چوتھا کلمہ")

    with col5:
                if st.button("kalma No 5 پانچواں کلمہ"):
                    #st.write("Button 55 clicked!")
                    st.image("Kalma-5.jpg", caption="Kalma 5 پانچواں کلمہ")

    with col6:
                if st.button("kalma No 6 چھٹا کلمہ"):
                    #st.write("Button 66 clicked!")
                    st.image("Kalma-6.jpg", caption="Kalma 6 چھٹا کلمہ")
       
    
    st.write("[2: Salah(Prayer)الصلاة](https://en.wikipedia.org/wiki/Salah)")
    st.markdown("<h5 style='text-align: center; color: green;'>Details of Rakats Are In Each Prayer with their Names</h5>", unsafe_allow_html=True)
    st.image("maxresdefault.jpg", caption="(الصلاة)")
    #st.write(':green[3: Zakat(Almsgiving)]الزكاة')
    st.write("[3: Zakat(Almsgiving)الزكاة](https://en.wikipedia.org/wiki/Zakat)")
    #st.markdown("<h4 style='text-align: center; color: green;'>Zakat الزكاة</h4>", unsafe_allow_html=True)
    st.image("zakat.jpg", caption="(الزكاة)")
    st.markdown("<h5 style='text-align: center; color: green;'>Detail Rules of Zakat in Islam زکوة اور اسلام میں اسکے مسائل </h5>", unsafe_allow_html=True)
    st.write("[:red[Zakat information in Islam]](https://www.wikihow.com/What-Is-Zakat-in-Islam)","[:green[زکوة اور اسلام میں اسکے مسائل]](https://www.urdupoint.com/islam/info/zakat.html)","[:red[Zakat Calculator]](https://www.urdupoint.com/calculators/zakat-calculator.html)")

    #st.write(':grey[4: Sawm(Fasting)]الصوم')
    st.write("[4: Sawm(Fasting)الصوم](https://en.wikipedia.org/wiki/Fasting_in_Islam)")
    st.image("Roja.jpg", caption="(الصوم)")
    st.markdown("<h5 style='text-align: center; color: green;'>Details of Fasting  روزہ کی فرضیت و فضیلت</h5>", unsafe_allow_html=True)
    st.write("[:red[روزہ کی فرضیت و فضیلت کے بارے میں کیا فرمایا گیا ہے؟]](https://www.irfan-ul-quran.com/urdu/qid/146/What-does-the-Qur-an-say-about-the-obligation-and-virtue-of-fasting)",
             "[:green[Fasting: Meaning & Rules]](https://fiqh.islamonline.net/en/fasting-meaning-rules/)",
             "[:red[Fasting during Ramadan]](https://en.wikipedia.org/wiki/Fasting_during_Ramadan)")
    st.write("[:green[رمضان کے متعلق 5 احادیث]](https://urdunotes.com/lesson/5-hadith-about-ramadan-in-urdu/)","[:red[रमजान के रोज़े की फ़ज़ीलत]](https://namazquran.com/ramzan-ke-roze-ki-fazilat/)",
              "[:green[رمضان المبارک کا استقبال اور اس کی عظمت و فضلیت]](https://urdu.premnathbismil.com/2024/10/ramzan-ul-mubarak-ka-istaqbal-ramzan-kaise-manae-ramzan-kya-hai.html.html)")


    #st.write(':red[5: Hajj(Pilgrimage)]الحج ')
    st.write("[5: Hajj(Pilgrimage)الحج](https://en.wikipedia.org/wiki/Hajj)")
    st.image("Hajj.jpg", caption="(حج)")
    st.markdown("<h5 style='text-align: center; color: green;'>Importance of Hajj  حج کی اہمیت</h5>", unsafe_allow_html=True)
    st.write("[:red[حج کی کیافضیلت ہے؟ | جامعہ علوم اسلامیہ علامہ محمد یوسف بنوری ٹاؤن]](https://www.banuri.edu.pk/readquestion/hajj-ki-fazilat-in-urdu-144512100022/08-06-2024)",
             "[:green[Manasik Of Hajj And Umrah Urdu]](https://archive.org/details/manasikofhajjandumrahurdu/mode/2up)")
    
    
    #,"[:red[Hajj Step by Step Infographics - Hajj Guidance Pictures]](https://hamariweb.com/islam/hajj-info-urdu/)")
    st.write("[:red[Hajj Step by Step Infographics - Hajj Guidance Pictures]](https://hamariweb.com/islam/hajj-info-urdu/)","[:green[Hajj ki Tareef our Masail - Dawat-e-Islami]](https://www.dawateislami.net/islamicportal/ur/farzuloom/hajj-ki-tareef-our-masail)")
    st.write("[:red[रमजान के रोज़े की फ़ज़ीलत]](https://namazquran.com/ramzan-ke-roze-ki-fazilat/)","[:green[हज - विकिपीडिया]](https://hi.wikipedia.org/wiki/%E0%A4%B9%E0%A4%9C)")
    st.markdown("<h5 style='text-align: center; color: green;'>Hajj information in video حج کی معلومات ویڈیو میں</h5>", unsafe_allow_html=True)    

    st.write("[Learn How to Perform Hajj Step By Step Complete Video(English)](https://www.youtube.com/watch?v=fngsHQ-Zv5s&t=111s)")
    st.write("[Complete Hajj Guide: Step-by-Step on how to make Hajj(English))](https://www.youtube.com/watch?v=iyOF_9cjGa0&t=26s)")
    st.write("[Hajj Ka Mukamal Tareeqa | Hajj step by step | How To Perform Hajj(Urdu)](https://www.youtube.com/watch?v=sBXRH9R2kWc)")
    st.write("[How to perform hajj step by step (Urdu)](https://www.youtube.com/watch?v=tkdbh1i29ao)")
    st.write("[Hajj Kay 5 Din-Hajj Ka Tariqa -The 5 Days Of Hajj-Abdul Habib Attari-(Urdu)](https://www.youtube.com/watch?v=E_3vvYt-olE)")   
    st.write("[Hajj Ka Tarika Abdul Habib Attari Islah e Aamaal Madina Jane Se Pahle Sun lain-(Urdu)](https://www.youtube.com/watch?v=fQmW8S6KEz0)")
    st.write("[Hajj 1928 coloured, Urdu with sound effects English subtitles #Hajj1928colour pilgrimage to mecca](https://www.youtube.com/watch?v=wdpjeGIkMoo)")
    st.write("[Purane zamany mein Hajj kaise hota tha? Purana Hajj 1924-1928 Purani Yaden  old Memories Makka ](https://www.youtube.com/watch?v=le-oRUvARJo)")
    st.write("[Old Hajj in 1950s Purana Hajj 1950 Makka](https://www.youtube.com/watch?v=ZdQW9x9DdHU)")
    st.write("[Old MAKKAH from 1700 to 2030 | mecca (makkah) future plan | Haram shareef expansion history](https://www.youtube.com/watch?v=_dI4TtXEgTs)")

             
    st.markdown("<h5 style='text-align: center; color: green;'>Complete information of the Holy Place Makkah</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: green;'>مقدس مقام مکہ مکرمہ کی مکمل معلومات</h5>", unsafe_allow_html=True)
    st.image("Makkahv.jpg", caption="(مسجد الحرام)")
    st.write("[Makkah](https://en.wikipedia.org/wiki/Mecca)")   
    st.write("[Masjeda Al Haram Makkah](https://en.wikipedia.org/wiki/Masjid_al-Haram)")  
    st.write("[Makkah Masjeda Al Haram Live 1](https://www.youtube.com/watch?v=eJNWHKld5E8)")
    st.write("[Makkah Masjeda Al Haram Live 2](https://www.youtube.com/watch?v=PPVvoWbReMI)")
    st.write("[Makkah Masjeda Al Haram Live 3](https://www.youtube.com/watch?v=bNY8a2BB5Gc)") 

    
    st.markdown("<h5 style='text-align: center; color: green;'>Complete information of the Holy Place Madinah</h5>", unsafe_allow_html=True)  
    st.markdown("<h5 style='text-align: center; color: green;'>مقدس مقام مدینہ منورہ کی مکمل معلومات</h5>", unsafe_allow_html=True) 
    st.image("Madinah.jpg", caption="(مسجد نبوی)")   
    st.write("[Madinah](https://en.wikipedia.org/wiki/Medina)")
    st.write("[Masjeda Al Nabwi Madinah ](https://simple.wikipedia.org/wiki/Al-Masjid_an-Nabawi)")
    st.write("[Madinah Masjeda Al Nabwi Live 1](https://www.youtube.com/watch?v=rHWSRMcGGBQ)")
    st.write("[Madinah Masjeda Al Nabwi Live 2](https://www.youtube.com/watch?v=yWw0DWJQVtU)")
    st.write("[Madinah Masjeda Al Nabwi Live 3](https://www.youtube.com/watch?v=naaOMgZbIHQ)")


    st.markdown("<h5 style='text-align: center; color: green;'>Complete information of the (Bayt al-Maqdis) Jerusalem</h5>", unsafe_allow_html=True) 
    st.markdown("<h5 style='text-align: center; color: green;'>یروشلم میں مسجد اقصیٰ کے بارے میں مکمل معلومات</h5>", unsafe_allow_html=True)  
    st.image("MasjedaAksa.jpg", caption="(مسجد اقصیٰ)")
    st.write("[Jerusalem](https://en.wikipedia.org/wiki/Jerusalem)")
    st.write("[Masjid al-Aqsa (Bayt al-Maqdis) Jerusalem](https://en.wikipedia.org/wiki/Al-Aqsa_Mosque)")    
    
    st.success('success')
    #balloowns
    st.balloons()

    
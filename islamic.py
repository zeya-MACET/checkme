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
    st.markdown("<h5 style='text-align: center; color: green;'>Details of Azan and its meaning</h5>", unsafe_allow_html=True)
    st.write("[Azan With Urdu Translation Full Azan Meaning in Urdu](https://www.youtube.com/watch?v=0Nx7qY9rikI)")
    st.write("[पूरी अजान तर्जुमा के साथ  Azan with hindi translation Azan ka tarjuma hindi Me ](https://www.youtube.com/watch?v=0Nx7qY9rikI)")
    st.write("[Namaz Tarjuma ke sath  Namaz Ka Tarika  Namaz With Urdu Translation  نماز کا طریقہ نماز ترجمہ ](https://www.youtube.com/watch?v=DgJ36yBDgQA)")




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

    
    st.markdown("<h5 style='text-align: center; color: green;'>SEERAT_UN_NABI سیرتِ النبی</h5>", unsafe_allow_html=True)  
    st.image("Seerat-un-Nabi.jpg", caption="(سیرتِ النبی)")  
    st.write("[सिरतून नबी (ﷺ) सीरीज | तरतीब (Index)](https://ummat-e-nabi.com/hi/seerat-un-nabi-series/)")
    st.write("[Complete Biography Of Prophet Muhammad PBUH  رسول اللہﷺ کی زندگی کی مکمل داستان  Seeratun Nabvi](https://www.youtube.com/watch?v=SN0irKWal7w)")
    st.write("[Qasas Ul-Anbiya In Urdu](https://archive.org/details/Qassas-ul-ambiya-ImamIbnKaseerInUrdu/mode/2up)")
    st.write("[Miracles Of Prophet Muhammad ﷺ  Complete Video  Mojzat e Rasool In Urdu](https://www.youtube.com/watch?v=f9JQ_gU5Qfo)")


    st.markdown("<h5 style='text-align: center; color: green;'>SEERAT UN NABI In Urdu Video - Chapter 1-40 By Sheikh Makki Al-Hijaazi</h5>", unsafe_allow_html=True)

    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 1) - audio only(English)](https://www.youtube.com/watch?v=jvW7CDx0-Wk&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=1)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 2) - audio only(English)](https://www.youtube.com/watch?v=24FVXN8s8q0&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=2)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 3) - audio only(English)](https://www.youtube.com/watch?v=PULbnO2LJbE&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=3)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 4) - audio only(English)](https://www.youtube.com/watch?v=TjHCLLv6jmE&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=4)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 5) - audio only(English)](https://www.youtube.com/watch?v=mdTz4AVt5KY&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=5)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 6) - audio only(English)](https://www.youtube.com/watch?v=kMLwrBayVHo&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=6)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 7) - audio only(English)](https://www.youtube.com/watch?v=1F4nRdVRTao&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=7)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 8) - audio only(English)](https://www.youtube.com/watch?v=DW2N_VKhIWU&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=8)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 9) - audio only(English)](https://www.youtube.com/watch?v=zbFkwPEcwa8&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=9)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 10) - audio only(English)](https://www.youtube.com/watch?v=xbdEynZ-u98&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=10)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 11) - audio only(English)](https://www.youtube.com/watch?v=UxQDwuQsmGI&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=11)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 12) - audio only(English)](https://www.youtube.com/watch?v=JrGUKDp6W2Y&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=13)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 13) - audio only(English)](https://www.youtube.com/watch?v=BT-DI6U4Lg4&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=13)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 14) - audio only(English)](https://www.youtube.com/watch?v=p2Lde7DQabg&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=40)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 15) - audio only(English)](https://www.youtube.com/watch?v=kOWUKrNNvQk&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=14)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 16) - audio only(English)](https://www.youtube.com/watch?v=1PEMtL4jIMI&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=15)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 17) - audio only(English)](https://www.youtube.com/watch?v=7CBvZ7iwCGM&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=16)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 18) - audio only(English)](https://www.youtube.com/watch?v=XDhjMX4C26w&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=17)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 19) - audio only(English)](https://www.youtube.com/watch?v=UHqIr_h5mVg&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=18)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 20) - audio only(English)](https://www.youtube.com/watch?v=v-HujpIbhYg&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=19)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 21) - audio only(English)](https://www.youtube.com/watch?v=E4vECgmtgng&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=20)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 22) - audio only(English)](https://www.youtube.com/watch?v=DWjw55cHVtg&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=21)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 23) - audio only(English)](https://www.youtube.com/watch?v=QxKR_jkJTtA&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=22)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 24) - audio only(English)](https://www.youtube.com/watch?v=0LBDrusRngg&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=23)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 25) - audio only(English)](https://www.youtube.com/watch?v=ujNIO2pSJ6Q&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=24)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 26) - audio only(English)](https://www.youtube.com/watch?v=8L2TpSmcIMM&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=26)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 27) - audio only(English)](https://www.youtube.com/watch?v=_Gz4N3OuJ28&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=25)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 28) - audio only(English)](https://www.youtube.com/watch?v=GA7hHANXSM4&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=27)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 29) - audio only(English)](https://www.youtube.com/watch?v=6RHrezeZZqU&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=28)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 30) - audio only(English)](https://www.youtube.com/watch?v=E_NjI7cyAnI&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=29)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 31) - audio only(English)](https://www.youtube.com/watch?v=GGvkt5YA5qw&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=30)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 32) - audio only(English)](https://www.youtube.com/watch?v=JJ4vlNcVMZQ&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=31)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 33) - audio only(English)](https://www.youtube.com/watch?v=npS2zlOJotU&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=32)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 34) - audio only(English)](https://www.youtube.com/watch?v=BLUVrOTPm4g&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=33)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 35) - audio only(English)](https://www.youtube.com/watch?v=bWlaGXNfV3c&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=34)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 36) - audio only(English)](https://www.youtube.com/watch?v=I39BcDzbeqo&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=36)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 37) - audio only(English)](https://www.youtube.com/watch?v=TRvbdRojAdM&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=35)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 38) - audio only(English)](https://www.youtube.com/watch?v=lTO1uwW8OI0&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=37)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 39) - audio only(English)](https://www.youtube.com/watch?v=56_VtEGzY-I&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=38)")
    st.write("[Seerat un Nabi Urdu - Maulana Makki (Chapter 40) - audio only(English)](https://www.youtube.com/watch?v=nO4yzaEA_OM&list=PLUX6avzb1ieuKbwsuPsnRv_6ttBFM8r9W&index=39)")




    st.markdown("<h5 style='text-align: center; color: green;'>QASASUL_AMBIYA قصص الأنبیاء</h5>", unsafe_allow_html=True) 
    st.image("QASASUL_AMBIYA.jpg", caption="(قصص الأنبیاء)")  
    st.write("[Qasas Ul-Anbiya In English](https://en.wikipedia.org/wiki/Qisas_al-Anbiya)")
    st.write("[Complete Story of All 25 Prophets of Islam(English)](https://myislam.org/prophet-stories/)")
    st.write("[Qasas Ul-Anbiya In Urdu](https://archive.org/details/Qassas-ul-ambiya-ImamIbnKaseerInUrdu/mode/2up)")

    st.markdown("<h5 style='text-align: center; color: green;'>All 25 Prophets whose name is mentioned in the Holy Quran Sharief</h5>", unsafe_allow_html=True)
    st.image("AllprophetsinQuran.jpg", caption="(قصص الأنبیاقرآن کریم میں 25 پیغمبروں کے نام آئے")  
    st.write("[1.	Adam (peace be upon him)  	    آدم عليه السلام](https://www.youtube.com/watch?v=WPDFJBtEtdI)")
    st.write("[2.	Idris (peace be upon him) 	    إدريس (عليه السلام](https://www.youtube.com/watch?v=odZAE2-8mtE)")
    st.write("[3.	Nuh (peace be upon him)		    نوح (عليه السلام](https://www.youtube.com/watch?v=2wIk7ZBqzVU)")
    st.write("[4.	Hud (peace be upon him)	  	    هود عليه السلام](https://www.youtube.com/watch?v=WY3srlGJLoY)")
    st.write("[5.	Saleh (peace be upon him)	    صالح عليه السلام](https://www.youtube.com/watch?v=Wus7TIlSkY8)")
    st.write("[6.	Ibrahim (peace be upon him)	    إبراهيم (عليه السلام](https://www.youtube.com/watch?v=v5dkl4W4g7E)")
    st.write("[7.	Ismail (peace be upon him)	    إسماعيل عليه السلام](https://www.youtube.com/watch?v=TP6MHJJNyLo)")
    st.write("[8.	Ishaq (peace be upon him)	    إسحاق عليه السلام](https://www.youtube.com/watch?v=OfCTTWRUmh0)")
    st.write("[9.	Lut (peace be upon him)		    لوط (عليه السلام](https://www.youtube.com/watch?v=nysUXjaSrwE)")
    st.write("[10.	Yaqub (peace be upon him)	    يعقوب عليه السلام](https://www.youtube.com/watch?v=Igzj4B9KkAU)")
    st.write("[11.	Yusuf (peace be upon him)	    يوسف عليه السلام](https://www.youtube.com/watch?v=Sl66TbxR08w)")
    st.write("[12.	Shu’aib (peace be upon him)	    شعيب عليه السلام](https://www.youtube.com/watch?v=8nrjUFlQqNE)")
    st.write("[13.	Ayyub (peace be upon him)	    أيوب عليه السلام](https://www.youtube.com/watch?v=yQLC1c_CDzY)")
    st.write("[14.	Dhulkifl (peace be upon him)    ذو الكفل عليه السلام](https://www.youtube.com/watch?v=USrR2zIMS-I)")
    st.write("[15.	Musa (peace be upon him)	    موسى عليه السلام](https://www.youtube.com/watch?v=YofZY_sJkZE)")
    st.write("[16.	Harun (peace be upon him)	    هارون عليه السلام](https://www.youtube.com/watch?v=8TVy16eV_5s)")
    st.write("[17.	Ilyas (peace be upon him)	    إلياس عليه السلام](https://www.youtube.com/watch?v=VIAcSlgNccQ)")
    st.write("[18.	Al-Yasa’ (peace be upon him)    اليسع عليه السلام ](https://www.youtube.com/watch?v=uBWihQ2UVsE)")
    st.write("[19.	Daud (peace be upon him)	    داود عليه السلام](https://www.youtube.com/watch?v=12l9nkdDU7c)")
    st.write("[20.	Sulayman (peace be upon him)    سليمان عليه السلام](https://www.youtube.com/watch?v=TecXMOlJY7o)")
    st.write("[21.	Yunus (peace be upon him)	    يونس عليه السلام](https://www.youtube.com/watch?v=IOdk5_TpYmI)")
    st.write("[22.	Zakariyya (peace be upon him)   زكريا عليه السلام](https://www.youtube.com/watch?v=UZA_74PKCtc)")
    st.write("[23.	Yahya (peace be upon him)	    يحيى عليه السلام](https://www.youtube.com/watch?v=cAaqk4cKMkY)")
    #st.write("[24.	Maryem (peace be upon him)	 	    عيسى عليه السلام](https://www.youtube.com/watch?v=X2m-z-Y5BXk)")
    st.write("[24.	Isa (peace be upon him)	 	    عيسى عليه السلام](https://www.youtube.com/watch?v=ZZZBviANn2c)")
    st.write("[25.	Muhammad (peace be upon him)    محمد صلى الله عليه وسلم](https://www.youtube.com/watch?v=y_CRCs5ssHw)")
    st.markdown("<h5 style='text-align: center; color: green;'>Qasas Ul-Anbiya In Urdu Video - Part 1-24 By Sheikh Makki Al-Hijaazi</h5>", unsafe_allow_html=True)
    st.write("[Qasas Ul-Anbiya In Urdu - Part 1 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=_SDYV2j77sM)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 2 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=saFUglDNH-o)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 3 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=Nbsy3vnfvUA)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 4 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=GQqIyxhwNNE)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 5 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=daPUxQSSqBs)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 6 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=-VjEYC_P_L8)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 7 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=mD2p-M0CAo0)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 8 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=bzick61REsM)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 9 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=67KhZCInFZA)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 10 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=Rbo_ylbfnlM)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 11 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=7HigZNMmP7s)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 12 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=H_HZFvYfAQ4)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 13 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=sLob-iVT4LA)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 14 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=gGKKfjpFZFQ)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 15 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=3_uFmTRt7Dg)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 16 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=urFR6_5cGhQ)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 17 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=elLcG-3nS-M)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 18 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=PwrPJ_kOY14)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 19 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=tEjXJnCHs-o)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 20 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=L_hXRWvNXyI)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 21 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=Ruxm22_7iQw)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 22 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=z2YPGKHIyK4)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 23 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=16CFY-w3Cew)")
    st.write("[Qasas Ul-Anbiya In Urdu - Part 24 - By Sheikh Makki Al-Hijaazi](https://www.youtube.com/watch?v=mAGebxTRs5c)")


    st.markdown("<h5 style='text-align: center; color: green;'>The importance of Duaa in Islam (اسلام میں دعا کی اہمیت)</h5>", unsafe_allow_html=True)
    st.image("Duaa.jpg", caption="( دعا کی اہمیت)") 
    st.write("[40 Rabbana Dua (Best Quranic Dua)](https://myislam.org/40-rabbana-dua-best-quranic-dua/)")
    st.write("[Islamic and Quranic Duas in Arabic with Translation](https://www.islamicfinder.org/duas/)")
    st.write("[45 Supplications (Duas) Every Muslim Should Know](https://thethinkingmuslim.com/2018/09/18/45-supplications-duas-every-muslim-should-know/)")
    st.write("[Dua in Arabic Text with English and Urdu explainations - Duas for daily use](https://www.islamicacademy.org/html/Dua/Dua.htm)")
    st.write("[Read Prayers & Daily Duas with English and Urdu Translation](https://www.urdupoint.com/islam/masnoon-duain/topic/prayers-and-daily.html)")


    st.markdown("<h5 style='text-align: center; color: green;'>99 Names of Allah (Al Asma ul Husna) اللہ کے 99 نام (الاسماء الحسنہ</h5>", unsafe_allow_html=True)
    st.image("Allah99Names.jpg", caption="(اللہ کے 99 نام (الاسماء الحسنہ) )") 
    st.write("[The 99 Names of Allah (SWT) with meaning](https://www.islamic-relief.org.uk/resources/knowledge-base/99-names-of-allah/)")
    st.write("[The 99 Names of Allah: In Arabic, Hindi, and English with Meanings](https://islamforall.in/the-99-names-of-allah-in-arabic-hindi-and-english-with-meanings/)")
    st.write("[99 Names of Allah in Hindi List – Meaning and Explanation](https://naat.operaking.in/99-names-of-allah-in-hindi-list-meaning-and-explanation)")
    st.write("[Allah 99 Names (Asma e Husna) Tarjuma in Urdu](https://archive.org/details/allah-99-names-asma-e-husna-tarjuma)")
    st.write("[99 NAMES OF ALLAH IN URDU TRANSLATION!Video ](https://www.bing.com/videos/riverview/relatedvideo?q=allah+99+names+with+urdu+translation&mid=FC47F986C43820F147D4FC47F986C43820F147D4&mcid=7F7A9A173EDF40D6B6825AC0622A30A3&FORM=VIRE)")
   
    st.markdown("<h5 style='text-align: center; color: green;'>importance Hadith in Islam اسلام میں حدیث کی اہمیت</h5>", unsafe_allow_html=True)
    st.image("Hadesh.jpg", caption="(اللہ کے 99 نام (الاسماء الحسنہ) )") 
    st.write("[List of hadith books](https://en.wikipedia.org/wiki/List_of_hadith_books#:~:text=The%20Nine%20Hadith%20books%20that%20are%20indexed%20in,Muwatta%20Imam%20Malik%2C%20Sunan%20al-Darimi%2C%20and%20Musnad%20Ahmad.)")
    st.write("[Sahih al Bukhari (English)](https://www.islamicfinder.org/hadith/bukhari/)")
    st.write("[Sahih al Bukhari (Urdu)](https://hamariweb.com/islam/hadith/sahih-bukhari-urdu/#:~:text=Sahih%20Bukhari%20in%20Urdu%20-%20Read%20complete%20Sahih,chapter%20name%2C%20references%20and%20in%20different%20languages%20translation.)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 1-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_1/)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 2-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_2/)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 3-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_3/)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 4-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_4/)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 5-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_5/)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 6-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_6/)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 7-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_7/)")
    st.write("[Sahih Bukhari Hadith in Urdu (All Volumes 8-8)](https://archive.org/details/SahihBukhariHadithInUrduAllVolumes1-8/Sahih_Bukhari-Volume_8/)")
    st.write("[Sahih al Muslim (English)](https://www.islamicfinder.org/hadith/muslim/)")  
    st.write("[Sahih Muslim Urdu Vol. 1-6 (صحیح مسلم) ](https://archive.org/details/sahih-muslim-arabic-urdu/sahih-muslim-urdu-vol-1/)")
    st.write("[Sahih Muslim Urdu Vol. 2-6 (صحیح مسلم) ](https://archive.org/details/sahih-muslim-arabic-urdu/sahih-muslim-urdu-vol-2/)")
    st.write("[Sahih Muslim Urdu Vol. 3-6 (صحیح مسلم) ](https://archive.org/details/sahih-muslim-arabic-urdu/sahih-muslim-urdu-vol-3/)")
    st.write("[Sahih Muslim Urdu Vol. 4-6 (صحیح مسلم) ](https://archive.org/details/sahih-muslim-arabic-urdu/sahih-muslim-urdu-vol-4/)")
    st.write("[Sahih Muslim Urdu Vol. 5-6 (صحیح مسلم) ](https://archive.org/details/sahih-muslim-arabic-urdu/sahih-muslim-urdu-vol-5/)")
    st.write("[Sahih Muslim Urdu Vol. 6-6 (صحیح مسلم) ](https://archive.org/details/sahih-muslim-arabic-urdu/sahih-muslim-urdu-vol-6/)")    
    st.success('success')
    #balloowns
    #st.balloons()

    
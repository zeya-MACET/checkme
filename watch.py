import streamlit as st
import pandas as pd
import streamlit as st
def app():
    #Title
    #st.title("welcome to My :blue[ACCOUNT] Page Website in Python")
    #Header
    #st.header(":blue[My General Information Page]")

    #st.button("Website Development is in Progress")
    #st.image(E:\My Development\Python\Website in Python\solar.png)
    #subheader
    
    #import streamlit as st

    #st.title("Google Search Bar in Streamlit")
    st.header(":blue[My General Information]")
    # Embed Google Search Bar
    google_search_html = """    
<div style="text-align:center;">
  <form action="https://www.google.com/search" method="get" target="_blank">
    <input type="text" name="q" placeholder="Type your search here..." style="width: 300px; height: 30px; font-size: 16px;">
    <input type="submit" value="Search" style="height: 36px; background-color: #4285F4; color: white; border: none; cursor: pointer;">
  </form>
</div>
"""

    # Display HTML using Streamlit's unsafe_html
    st.markdown(google_search_html, unsafe_allow_html=True)

    #text
    #st.text(''' Helloe Everyone Welcome to my Python Station Streamlit 
            #Hope you will check it......''')
    #bbchindinews=("BBC HINDI https://www.bbc.com/hindi")

    #st.write(bbchindinews)
    #############################################################################################
    # Create a dropdown list
    #selected_option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

    # Display the selected option
    #st.write(f"You selected: {selected_option}")
    ##############################################################################################
    st.subheader(':green[My News Collection]')

    ############$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Create a sample dataframe
    data = {
    'Category': ['Arabic ', 'English ', 'Arabic ', 'Hindi ', 'Urdu ',
                 'English ', 'Urdu ', 'Hindi ', 'Arabic ', 'Hindi ', 'English '
                 , 'English ', 'English ', 'English ', 'English ', 'Urdu ', 'Urdu ', 'Urdu ', 'Arabic ', 'Arabic ', 'Arabic ', 'English ', 'Hindi ', 'Hindi '],
    'Subcategory': ['Alwatan https://www.alwatan.com.sa/', 'Saudigazette https://pdf.saudigazette.com.sa/', 'Okaz https://www.okaz.com.sa/', 
                    'Dainak Jagran https://www.jagran.com/', 'Siasat https://epaper.siasat.com/','Arabnews https://www.arabnews.com/saudiarabia/', 
                    'Inquilab https://www.inquilab.com/', 'NDTV https://ndtv.in/', 'Makkah https://makkahnewspaper.com/', 'BBC https://www.bbc.com/hindi/', 'The Indian Express https://indianexpress.com/'
                    , 'CNN https://edition.cnn.com/', 'Times of India https://timesofindia.indiatimes.com//', 'Hindustan Times https://www.hindustantimes.com/', 'Alzagira https://www.aljazeera.com/'
                    , 'Qaumitanzeem https://qaumitanzeem.com/', 'Qaumiawaz https://www.qaumiawaz.com/', 'Taasir https://epaper.taasir.com/page.php'
                    , 'Aljazeera https://www.aljazeera.net/', 'Aawsat https://aawsat.com/', 'BBC https://www.bbc.com/arabic', 'BBC https://www.bbc.com/', 'Dainak Bhaskar https://www.bhaskar.com/'
                    , 'Navbharattimes https://navbharattimes.indiatimes.com/headlines.cms']
    }
    df = pd.DataFrame(data)

    # Create the primary dropdown for Category
    selected_category = st.selectbox("Select the Language ", df['Category'].unique())

    # Filter the dataframe based on the selected category
    filtered_df = df[df['Category'] == selected_category]

    # Create the dependent dropdown for Subcategory
    selected_subcategory = st.selectbox("Select  Newswebsite", filtered_df['Subcategory'].unique())

    # Display the selected options
    st.write(f":green[You selected:] :red[{selected_category}] - {selected_subcategory}")
    ############$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    #write
    #st.write('Please Subscribe my Python Channel')
    #Image and Caption
    from PIL import Image
    img = Image.open('enews.png')
    st.image(img,caption='News on the Web')
    #Colourful text
    #success
    st.success('success')
    #Error
    
    #balloowns
    st.balloons()



 


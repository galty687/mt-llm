import requests

import streamlit as st

#google_translate_api_key = st.secrets['google_translate_api_key']

def translate_text_with_api_key(text, target_language):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'q': text,
        'target': target_language,
        'key': 'AIzaSyBqPMziyFdXzb4NuafTSFS2fRxjFik4K6k' 
    }
    response = requests.post(url, params=params)
    translation = response.json()

print(translate_text_with_api_key("Hello, world!", "zh_CN"))    
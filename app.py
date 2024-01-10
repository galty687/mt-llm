import streamlit as st
from openai import OpenAI
import requests

# 实例化OpenAI对象，并设置API key
client = OpenAI(api_key=st.secrets['openai_api_key'])

# 配置Google Cloud Translate API key
google_translate_api_key = st.secrets['google_translate_api_key']

# 清理输入的文本，主要是去除不必要的换行。
def cleaning_text_with_chatgpt(text):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You are an expert editor speicalized in reviewing."},
            {"role": "user", "content": f'Please remove all unnecessary line breaks of the following text:{text}'}
            ]
        )
        cleaned_text = completion.choices[0].message.content
        return cleaned_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# 定义基于 Google Translate API的翻译函数
def translate_text_with_google(text, target_language):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'q': text,
        'target': target_language,
        'key': google_translate_api_key  # Replace with your actual API key
    }
    response = requests.post(url, params=params)
    
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    translation = response.json()
    # Extract the translated text
    translated_text = translation.get('data', {}).get('translations', [{}])[0].get('translatedText', '')
    return translated_text    

# 使用ChatGPT进行翻译

def translate_with_chatgpt(text, target_language):
    try:
        completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
       
        messages=[
            {"role": "system", "content": "You are an translation expert."},
            {"role": "user", "content": f'Please translate the following text into {target_language}. Output the translation only. \n Text to translate: {text}'}
        ]
        )
        cleaned_text = completion.choices[0].message.content
        return cleaned_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# 使用Chat对原文和译文进行编辑
def editing_with_chatgpt(source, target):
    try:
        completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
       
        messages=[
            {"role": "system", "content": "You are an translation expert."},
            {"role": "user", "content": f'Please polish the following translation. Output the translation only. No need to explain. \n source: {source} \n target: {target}'}
        ]
        )
        cleaned_text = completion.choices[0].message.content
        return cleaned_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# 使用ChatGPT对译文进行审校，并输出结果。
def review_with_chatgpt(text):
    try:
        completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
       
        messages=[
            {"role": "system", "content": "You are an native expert proofreader"},
            {"role": "user", "content": f'Please polish the text to make it more readable to {target_language} readers. Output the final text only. \n text: {text}'}
        ]
        )
        reviewed_text = completion.choices[0].message.content
        return reviewed_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# 定义了使用Google Translate API的翻译函数
    



def review_text_with_openai(text):
    # Implement OpenAI text review (based on your OpenAI setup)
    reviewed_text = "reviewed text here"  # Replace with actual reviewed text from OpenAI
    return reviewed_text

# Streamlit interface
st.title('智能翻译系统')

# Text input
input_text = st.text_area("Enter text:")

# Language selection for translation
target_language = st.selectbox(
    "Select target language:",
    ["zh-CN","en"]
)



if st.button('Smart Translate'):
    if input_text:
        with st.spinner('生成四种版本中... 耗时较长，请稍候。'):
                
            cleaned_text = cleaning_text_with_chatgpt(input_text)
            translated_text_google = translate_text_with_google(cleaned_text, target_language)
            translate_text_with_chatgpt= translate_with_chatgpt(cleaned_text, target_language)
            edited_text = editing_with_chatgpt(cleaned_text,translated_text_google)
            reviewed_text = review_with_chatgpt(edited_text)



        #st.write("Cleaned Text:", cleaned_text)
        st.subheader("谷歌翻译版本:")    
        st.write(translated_text_google)
        st.write('---')

        st.subheader("ChatGPT翻译版本:")    
        st.write(translate_text_with_chatgpt)
        st.write('---')

        st.subheader("谷歌翻译, Chatgpt润色:")    
        st.write(edited_text)
        st.write('---')

        st.subheader("母语审校:")
        st.write(reviewed_text)

        st.success('成功完成')
    else:
        st.write("Please enter some text to get translated.")

if st.button('谷翻模润'):
    if input_text:
        with st.spinner('谷歌翻译, Chatgpt润色中，请稍候。'):

            cleaned_text = cleaning_text_with_chatgpt(input_text)
            translated_text_google = translate_text_with_google(cleaned_text, target_language)
            edited_text = editing_with_chatgpt(cleaned_text,translated_text_google)
            


        st.subheader("谷歌翻译, Chatgpt润色:")    
        st.write(edited_text)
        st.write('---')
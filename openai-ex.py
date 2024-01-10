from openai import OpenAI
import streamlit as st




client = OpenAI(api_key=st.secrets['openai_api_key'])

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an expert translator."},
    {"role": "user", "content": 'Please translate the following sentence into Chinese: How is everything going?'}
  ]
)

print(completion.choices[0].message.content)
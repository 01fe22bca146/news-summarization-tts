import streamlit as st
import requests

st.title("News Summarization & Sentiment Analysis")

company = st.text_input("Enter Company Name", "Tesla")

if st.button("Analyze"):
    response = requests.get(f"http://127.0.0.1:8000/get-news/{company}")
    data = response.json()
    
    st.write("## Sentiment Analysis")
    st.json(data)
    
    tts_response = requests.get(f"http://127.0.0.1:8000/generate-tts/{company}")
    audio = tts_response.json()["audio"]
    st.audio(audio)

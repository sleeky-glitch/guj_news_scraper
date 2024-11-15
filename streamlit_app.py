import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from translate import Translator
from datetime import datetime
import re

# Set page configuration
st.set_page_config(
    page_title="Gujarati News Scraper",
    page_icon="📰",
    layout="wide"
)

# Custom CSS to improve appearance
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
    }
    .stTitle {
        color: #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize translation cache
if 'translation_cache' not in st.session_state:
    st.session_state.translation_cache = {}

# Function to translate Gujarati to English with caching
def translate_text(text, dest='en'):
    if text in st.session_state.translation_cache:
        return st.session_state.translation_cache[text]
    
    translator = Translator(to_lang=dest)
    try:
        translation = translator.translate(text)
        st.session_state.translation_cache[text] = translation
        return translation
    except:
        return text

# Function to clean text
def clean_text(text):
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to scrape Divya Bhaskar
def scrape_divya_bhaskar(search_term):
    url = f"https://www.divyabhaskar.co.in/search?q={search_term}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        

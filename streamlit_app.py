import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from translate import Translator
import time

# Set page configuration
st.set_page_config(
    page_title="Gujarati News Scraper",
    page_icon="📰",
    layout="wide"
)

# Function to translate text with delay to avoid rate limiting
def translate_text(text, from_lang='gu', to_lang='en'):
    try:
        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        # Add delay to avoid translation service rate limits
        time.sleep(0.5)
        return translator.translate(text)
    except:
        return text

# Function to scrape Divya Bhaskar
def scrape_divya_bhaskar(search_term, max_articles=5):
    url = f"https://www.divyabhaskar.co.in/search?q={search_term}"


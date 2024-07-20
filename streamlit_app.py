import streamlit as st
import os
os.system("wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chrome-linux64.zip"
os.system("unzip chrome-linux64.zip"
"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

   
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = webdriver.Chrome("./chromedriver",options=options)
    driver.get("https://myco.io/")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
    print("done")

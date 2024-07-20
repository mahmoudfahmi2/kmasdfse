import streamlit as st
import os
os.system("wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip")
os.system("unzip chromedriver-linux64.zip")

with st.echo():
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = webdriver.Chrome("./chromedriver-linux64/chromedriver",options=options)
    driver.get("https://myco.io/")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
    print("done")

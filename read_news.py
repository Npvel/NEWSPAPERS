import streamlit as st
import webbrowser

import time

import os
import pathlib
from pathlib import Path

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH', 
                                os.path.join(BASE_DIR, "chromedriver_win32", "chromedriver.exe"))

HEADLESS_MODE = bool(os.getenv("HEADLESS_MODE", False))

chromeOptions = webdriver.ChromeOptions()
if HEADLESS_MODE:
    chromeOptions.headless = True
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument("--disable-blink-features")
# chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
chromeOptions.add_experimental_option('useAutomationExtension', False)



s=Service(CHROMEDRIVER_PATH)
url = 'https://auth.rbc.ru/loginpro?tab=enter&from=login_toplinepro&host=https%3A%2F%2Fpro.rbc.ru&pathname=%2F&project=rbcpro'

if st.button('RBC PRO'):
    

    browser = webdriver.Chrome(service=s, options=chromeOptions)
    # 
    # browser = webdriver.Chrome(service=s, executable_path=config.CHROMEDRIVER_PATH, chrome_options=chromeOptions)

    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            const newProto = navigator.__proto__
            delete newProto.webdriver
            navigator.__proto__ = newProto
            """
        })

    wait = WebDriverWait(browser, 60)


    # webbrowser.open_new_tab()

    browser.get(url)

    time.sleep(5)

    email = browser.find_elements(By.CSS_SELECTOR, "input[class='paywall__auth-pro__form__input js-paywall-auth-input']")
    email[3].send_keys('Vladimir.Ruchkin@eulerhermes.com')

    password = browser.find_elements(By.CSS_SELECTOR, "input[class='paywall__auth-pro__form__input js-paywall-auth-input']")
    password[4].send_keys('87654321')

    button_enter = browser.find_elements(By.CSS_SELECTOR,"input[type='submit']")
    browser.execute_script("arguments[0].click();", button_enter[1])

    
    # session_state.url = url

    # webbrowser.open_new_tab(url)

    # url = 'https://pro.rbc.ru/info-service/api/v2/ev/?ts=1657123513827'



# browser.find_element(By.CSS_SELECTOR, "a[class='topline__auth-pro__link js-topline-profile-link']").click()
    
# email = browser.find_elements(By.CSS_SELECTOR, "input[class='paywall__auth-pro__form__input js-paywall-auth-input']")
# # browser.execute_script("arguments[0].send_keys('Vladimir.Ruchkin@eulerhermes.com');", email[0])
# # email[0].send_keys('Vladimir.Ruchkin@eulerhermes.com')
# print(email)
# # email.send_keys('Vladimir.Ruchkin@eulerhermes.com')
# # email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form[class='paywall__auth-pro__form js-login-validate']")))
# # # browser.execute_script("arguments[0].send_keys('Vladimir.Ruchkin@eulerhermes.com');", email)
# # email.send_keys('Vladimir.Ruchkin@eulerhermes.com')

# # password = browser.find_element(By.XPATH, "//*[text()[contains(., 'пароль')]]")
# # # browser.execute_script("arguments[0].send_keys('87654321');", password)
# # password.send_keys('87654321')
# # time.sleep(1)


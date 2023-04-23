from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
LOG_ERROR = 2
query = input("Enter your search term ")
input = input("Would you like to search google or youtube? G/Y? ")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def googlesearch(query):
    browser.get('https://www.google.com/')
    search = browser.find_element(by=By.NAME, value="q")
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
    try:
        search = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
    finally:
        results = browser.find_elements(by=By.TAG_NAME, value="h3")
    for item in results:
        print(item.text)

def ytsearch(query):
    browser.get('https://www.youtube.com/')
    time.sleep(2)
    search = browser.find_element(by=By.NAME, value="search_query")
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
    try:
        search = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "title-wrapper"))
        )
    finally:
        videotitles = browser.find_elements(by=By.ID, value="title-wrapper")
    for item in videotitles:
        print(item.text)

if input.upper() == "G":
    googlesearch(query)
else: 
    ytsearch(query)

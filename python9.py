# USING EXTERNAL PACKAGE
# import python4

# print(python4.randomNum(15))

# import requests
# from bs4 import BeautifulSoup

# header = {
#     "Accept": "*/*",
#     "Accept-Encoding": 'gzip',
#     "Accept-Language": "en-US",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
# }


# response = requests.post("https://www.walmart.com/account/login?vid=oaoh&tid=0&returnUrl=%2F", data={
#     "email": "example@example.com",
#     "password": "password"
# }, headers=header)

# soup = BeautifulSoup(response.content)

# print(soup.prettify())
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")

sleep(10)
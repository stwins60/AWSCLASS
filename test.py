from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Chrome:
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def openSite(self):
        return self.driver.get(self.url)

class Firefox:
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def openSite(self):
        return self.driver.get(self.url)



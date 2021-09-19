from selenium import webdriver
from selenium.webdriver.common.by import By

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com")
        login = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login.click()
        # full xpath
        # /html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a
        # xpath
        # //*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a

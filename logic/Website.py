from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
class Website:
    def __init__(self):
        pass
    def getTicket(self,url:str,class_:str, type:str, driver:webdriver.Firefox):
        driver.get(url)
        try:
            time.sleep(5)
            elements = driver.find_elements(type, class_)
            if not elements:
                return 0
            else:
                print(url)
        except:
            return 0
        
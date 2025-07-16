from selenium import webdriver
from logic.Website import Website
import time
from datetime import datetime, timedelta
class Tracker:
    _website = None
    _driver = None
    def __init__(self):
        self._website = Website()
        self._driver = webdriver.Firefox()
    def tracking(self, argsList:list, sleepPersite:int, limitTry:int, sleepPerTry:int):
        for i in range(limitTry):
            for args in argsList:
                self._website.getTicket(args.get("url"),args.get("class"),args.get("args"),self._driver)
                time.sleep(sleepPersite)
            time.sleep(sleepPerTry)
        self._driver.quit()

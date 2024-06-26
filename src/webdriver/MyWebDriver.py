import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils.SleepTime import SleepTime

class MyWebDriver:
    def __init__(self, driver: webdriver.Chrome, url: str) -> None:
        self._driver = driver
        self._url = url

    @staticmethod
    def of(url: str) -> object:
        driver = webdriver.Chrome()
        return MyWebDriver(driver, url)
    
    def run(self):
        self.driverOpen()

    @SleepTime(2)
    def driverOpen(self) -> None:
        self._driver.get(self._url)
    
    @SleepTime(2)
    def clickBtn(self, value_type: By, value: str) -> None:
        btn = self._driver.find_element(value_type, value)
        ActionChains(self._driver).click(btn).perform()
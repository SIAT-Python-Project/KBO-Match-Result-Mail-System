import os
import sys

from selenium.webdriver.chrome.webdriver import WebDriver as Chrome

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from PlayerCrawler import PlayerCrawler
from domain.Pitcher import Pitcher

class PitcherCrawler(PlayerCrawler):
    def __init__(self, driver: webdriver.Chrome, url: str, tableColNumbers: list[int]) -> None:
        super().__init__(driver, url, tableColNumbers)

    @staticmethod
    def of() -> object:
        driver = webdriver.Chrome()
        url = 'https://www.koreabaseball.com/Record/Player/PitcherBasic/BasicOld.aspx'
        tableColNumbers = [3, 4, 8, 19]

        return PitcherCrawler(driver, url, tableColNumbers)
        
    def create_player(self, row) -> Pitcher:
        player_info = [row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a').text]
        
        for idx in self._tableColNumbers:
            player_info.append(row.find_element(By.CSS_SELECTOR, f'td:nth-child({idx})').text)

        return Pitcher.of(*player_info)
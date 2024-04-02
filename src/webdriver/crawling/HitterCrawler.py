import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from PlayerCrawler import PlayerCrawler
from domain.Hitter import Hitter

class HitterCrawler(PlayerCrawler):
    def __init__(self, driver: webdriver.Chrome, url: str, tableColNumbers: list[int]) -> None:
        super().__init__(driver, url, tableColNumbers)

    @staticmethod
    def of() -> object:
        driver = webdriver.Chrome()
        url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx'
        tableColNumbers = [3, 4, 8, 11, 12, 13]

        return HitterCrawler(driver, url, tableColNumbers)
        
    def create_player(self, row) -> Hitter:
        player_info = [row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a').text]
        
        for idx in self._tableColNumbers:
            player_info.append(row.find_element(By.CSS_SELECTOR, f'td:nth-child({idx})').text)

        return Hitter.of(*player_info)
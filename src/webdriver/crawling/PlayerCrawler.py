import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver.MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime
from selenium.common.exceptions import NoSuchElementException

class PlayerCrawler(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str, tableColNumbers: list[int]) -> None:
        super().__init__(driver, url)
        self._tableColNumbers = tableColNumbers

    def run(self) -> list[object]:
        self.driverOpen()
        self.clickBtn(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_udpContent > div.record_result > table > thead > tr > th:nth-child(5) > a')
        self.focus_display()
        players = self.get_player_info()

        return players


    @SleepTime(2)
    def focus_display(self) -> None:
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_player_info(self) -> list[object]:
        page_count = self.get_page_count()

        players = []

        for count in range(1, page_count+1):
            self.clickBtn(By.ID, f'cphContents_cphContents_cphContents_ucPager_btnNo{count%5 if count%5 != 0 else 5}')
            
            players += self.crawl_player_info()

            if count != page_count and count % 5 == 0:
                self.clickBtn(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnNext')

        return players

    def get_page_count(self) -> int:
        try:
            self.clickBtn(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnLast')
            
            page_btns = self._driver.find_elements(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_udpContent > div.record_result > div > a')
            count = int(page_btns[-2].text)
            
            self.clickBtn(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnFirst')

            return count
        except NoSuchElementException:
            return 1

    def crawl_player_info(self) -> list[object]:
        rows = self._driver.find_elements(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
        
        return [self.create_player(row) for row in rows]
            
    def create_player(self, row):
        pass
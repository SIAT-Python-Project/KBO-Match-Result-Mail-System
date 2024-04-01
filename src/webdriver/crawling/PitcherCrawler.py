import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime
from domain.Pitcher import Pitcher
from selenium.common.exceptions import NoSuchElementException

class PitcherCrawler(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str) -> None:
        super().__init__(driver, url)

    @staticmethod
    def of():
        return PitcherCrawler(webdriver.Chrome(), 'https://www.koreabaseball.com/Record/Player/PitcherBasic/BasicOld.aspx')
    
    def run(self) -> list[Pitcher]:
        self.driverOpen()
        self.focus_display()
        pitchers = self.get_pitcher_info()

        return pitchers
    

    @SleepTime(2)
    def focus_display(self) -> None:
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_pitcher_info(self) -> list[Pitcher]:
        page_count = self.get_page_count()

        hitters = []

        for count in range(1, page_count+1):
            self.clickBtn(By.ID, f'cphContents_cphContents_cphContents_ucPager_btnNo{count%5 if count%5 != 0 else 5}')
            
            hitters += self.crawl_pitcher_info()

            if count != page_count and count % 5 == 0:
                self.clickBtn(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnNext')

        return hitters

    def get_page_count(self) -> int:
        try:
            self.clickBtn(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnLast')
            
            page_btns = self._driver.find_elements(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_udpContent > div.record_result > div > a')
            count = int(page_btns[-2].text)
            
            self.clickBtn(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnFirst')

            return count
        except NoSuchElementException:
            return 1

    def crawl_pitcher_info(self) -> list[Pitcher]:
        rows = self._driver.find_elements(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
        
        return [self.create_pitcher(row) for row in rows]
            
    def create_pitcher(self, row):
        name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a').text
        team = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        earnedRunsAverage = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
        win = row.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
        strikeOuts = row.find_element(By.CSS_SELECTOR, 'td:nth-child(19)').text

        return Pitcher(name, team, earnedRunsAverage, win, strikeOuts)
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime
from domain.Hitter import Hitter
from selenium.common.exceptions import NoSuchElementException

class HitterCrawler(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str) -> None:
        super().__init__(driver, url)

    @staticmethod
    def of():
        return HitterCrawler(webdriver.Chrome(), 'https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx')
    
    def run(self) -> list[Hitter]:
        self.driverOpen()
        self.focus_display()
        hitters = self.get_hitter_info()

        return hitters

    @SleepTime(2)
    def focus_display(self) -> None:
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_hitter_info(self) -> list[Hitter]:
        page_count = self.get_page_count()

        hitters = []

        for count in range(1, page_count+1):
            self.clickBtn(By.ID, f'cphContents_cphContents_cphContents_ucPager_btnNo{count%5 if count%5 != 0 else 5}')
            
            hitters += self.crawl_hitter_info()

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

    def crawl_hitter_info(self) -> list[Hitter]:
        rows = self._driver.find_elements(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
        
        return [self.create_hitter(row) for row in rows]
            
    def create_hitter(self, row):
        name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a').text
        team = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        avg = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
        hit = row.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
        homeRun = row.find_element(By.CSS_SELECTOR, 'td:nth-child(11)').text
        runBattedIn = row.find_element(By.CSS_SELECTOR, 'td:nth-child(12)').text
        stolenBase = row.find_element(By.CSS_SELECTOR, 'td:nth-child(13)').text

        return Hitter(name, team, avg, hit, homeRun, runBattedIn, stolenBase)
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime
import datetime
from datetime import timedelta
from domain.News import News

class NewsCrawler(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str, teams:list[str]) -> None:
        super().__init__(driver, url)
        self.teams = teams
    
    @staticmethod
    def of(teams) -> object:
        driver = webdriver.Chrome()
        url = "https://www.koreabaseball.com/MediaNews/News/BreakingNews/List.aspx"
        return NewsCrawler(driver, url, teams)
    
    def run(self):
        self.driverOpen()
        return_news_list = self.news_crawling()
        return return_news_list
    
    @SleepTime(2)    
        
    def news_crawling(self) -> list[object]:       
        self.news_date_element = self._driver.find_elements(By.CLASS_NAME,'date')       # 발행날짜
        self.news_title_element = self._driver.find_elements(By.CSS_SELECTOR,'.txt strong') # 제목
        self.news_link_element = self._driver.find_elements(By.CSS_SELECTOR,'.txt strong a')    # 뉴스 링크
        
        return self.content_text()
         

    # 어제 날짜 가져오기
    def day(self):
        yesterday = datetime.date.today() - timedelta(days=1)       # 어제 날짜 가져오기
        yesterday = yesterday.strftime('%Y.%m.%d')             # 전처리
        return yesterday

    
    # 뉴스 타이틀, 링크 가져오기
    def content_text(self) -> News:
        news_list = []
        
        for i in range(0,len(self.news_date_element)):
            if self.day() == self.news_date_element[i].text:
                for team_list in self.teams:
                    if team_list in self.news_title_element[i].text:
                        news_title = self.news_title_element[i].text
                        news_link = self.news_link_element[i].get_attribute('href')
                        news_list.append(News.of(self.teams, news_title, news_link))
       
       
        return news_list
    

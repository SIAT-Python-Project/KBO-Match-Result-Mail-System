import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime

class TeamRankCrawler(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str ) -> None:
        super().__init__(driver, url)
        

    @staticmethod
    def of(url: str) -> object:
        driver = webdriver.Chrome()
        url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"   
        return TeamRankCrawler(driver, url)
    
    def run(self):
        self.driverOpen()
        team_rank = self.get_rank_list()
        return team_rank
        
    
    @SleepTime(2)
    def teamRankList(self) -> list[object]:
        get_team_rank = self.get_rank_list()
        return get_team_rank
    
        
    def get_rank_list(self) -> list[object]:
        team_rank_list = []
        
        # 목차(전체)
        team_head = self._driver.find_element(By.CSS_SELECTOR, '.tData thead tr')    
        team_rank_list.append(team_head)
        
        # 팀 순위 가져오기
        for i in range(1,11):
            team_rank = self._driver.find_elements(By.CSS_SELECTOR, '.mb25 + .tData tbody tr:nth-child('+str(i)+')') 
            team_rank_list += team_rank
        return team_rank_list
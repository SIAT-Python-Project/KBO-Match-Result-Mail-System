import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime
from domain.TeamRank import TeamRank

class TeamRankCrawler(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str ) -> None:
        super().__init__(driver, url)
        

    @staticmethod
    def of() -> object:
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
        team_rank_total = []

        
        # 팀 순위 가져오기
        for i in range(1,11):
            team_rank = self._driver.find_elements(By.CSS_SELECTOR, '.mb25 + .tData tbody tr:nth-child('+str(i)+')')
            team_rank_total.append(TeamRank([rank_team.text for rank_team in team_rank]))
        

        return team_rank_total
    


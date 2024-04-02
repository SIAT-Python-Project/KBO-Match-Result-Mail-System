import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime



class TeamRankCrawler(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str) -> None:
        super().__init__(driver, url)
        

    @staticmethod
    def of(url: str) -> object:
        driver = webdriver.Chrome()
        url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"   
        return TeamRankCrawler(driver, url)
    
    def run(self):
        self.driverOpen()
        self.teamRankList()
        
    
    @SleepTime(2)
    def teamRankList(self):
        self.get_head_rank_list()
        self.get_rank_list()
        
    def get_head_rank_list(self):
        team_head_list= []
        team_head = self._driver.find_elements(By.CSS_SELECTOR, '.tData thead tr th')    # 목차
        team_head_list.append(team_head)
        print(team_head_list[0][1].text)
        
    def get_rank_list(self):
        team_rank_list = []
        for i in range(1,11):
            team_rank = self._driver.find_elements(By.CSS_SELECTOR, '.mb25 + .tData tbody tr td:nth-child('+str(i)+')') # 순위 ~ 연승까지 가져오기
            team_rank_list.append(team_rank)
            
        self.create_team_rank(team_rank_list)
        self.create_team_name(team_rank_list)
        self.create_game(team_rank_list)
        self.create_game_win(team_rank_list)
        self.create_game_lost(team_rank_list)
        self.create_game_draw(team_rank_list)
        self.create_percent_win(team_rank_list)
        self.create_game_back(team_rank_list)
        self.create_recent_game(team_rank_list)
        self.create_game_steak(team_rank_list)
            
    def create_team_rank(self, row_rank):
        rank_list = []
        for i in range(0,10):
            rank_list.append(row_rank[0][i])
        print(rank_list[1].text)
            
    def create_team_name(self, row_team_name):
        team_name_list = []
        for i in range(0,10):
            team_name_list.append(row_team_name[1][i])
        print(team_name_list[1].text)
    
    def create_game(self, row_game):
        game_count_list = []
        for i in range(0,10):
            game_count_list.append(row_game[2][i])
        print(game_count_list[1].text)
        
    def create_game_win(self, row_game_win):
        game_win_count_list = []
        for i in range(0,10):
            game_win_count_list.append(row_game_win[3][i])
        print(game_win_count_list[1].text)
        
    def create_game_lost(self, row_game_lost):
        game_lost_count_list = []
        for i in range(0,10):
            game_lost_count_list.append(row_game_lost[4][i])
        print(game_lost_count_list[1].text)
        
    def create_game_draw(self, row_game_draw):
        game_draw_count_list = []
        for i in range(0,10):
            game_draw_count_list.append(row_game_draw[5][i])
        print(game_draw_count_list[1].text)
    
    def create_percent_win(self, row_percent_win):
        percent_win_list = []
        for i in range(0,10):
            percent_win_list.append(row_percent_win[6][i])
        print(percent_win_list[1].text)   
         
    def create_game_back(self, row_game_back):
        game_back_list = []
        for i in range(0,10):
            game_back_list.append(row_game_back[7][i])
        print(game_back_list[1].text)   
         
    def create_recent_game(self, row_recent_game):
        recent_game_list = []
        for i in range(0,10):
            recent_game_list.append(row_recent_game[8][i])
        print(recent_game_list[1].text)
            
    def create_game_steak(self, row_game_steak):
        game_steak_list = []
        for i in range(0,10):
            game_steak_list.append(row_game_steak[9][i])
        print(game_steak_list[1].text)    
        
TeamRankCrawler(webdriver.Chrome(),"https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx").run()

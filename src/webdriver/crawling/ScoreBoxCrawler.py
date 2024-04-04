import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from MyWebDriver import MyWebDriver
from utils.SleepTime import SleepTime
from domain.ScoreBox import GameResult


class Boxscore(MyWebDriver):
    def __init__(self, driver: webdriver.Chrome, url: str) -> None:
        super().__init__(driver, url)
        
    
    @staticmethod
    def of() -> object:
        driver = webdriver.Chrome()
        url = "https://www.koreabaseball.com/Schedule/ScoreBoard.aspx"
        return Boxscore(driver, url)
    
    def run(self):
        self.driverOpen()
        self.clickBtn(By.CLASS_NAME, 'prev')
        game_set = self.score_bord()
        return game_set
    
    @SleepTime(2) 
    def score_bord(self) -> list[object]:
        inning = []
        game_result = []
        inning_element = self._driver.find_elements(By.CSS_SELECTOR, '.tScore tr')
        for i in range(len(inning_element)):
            inning.append(inning_element[i].text)
        
        game_result = []
        for i in range(0,len(inning),3):
            game_result.append(inning[i:i+3])

        return game_result    


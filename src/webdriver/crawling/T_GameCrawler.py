import os
import pandas as pd
import requests
from webdriver.crawling.Scraper import Scraper
from bs4 import BeautifulSoup
from datetime import datetime
from domain.T_Game import T_Game
from typing import List

class GameInfoScraper(Scraper):
    def __init__(self, url):
        super().__init__(url)

    def scrape_data(self):
        home_teams = []
        away_teams = []
        stadiums = []
        schedule_times = []
        game_dates = []

        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        vsbox_list = soup.find_all("div", class_="vsbox")
        v_info_list = soup.find_all("div", class_="v_info")

        time_elements = [vinfo.find("span", class_="time") for vinfo in v_info_list]
        schedule_times = [time.text.strip() for time in time_elements[5:]]

        box_head = soup.find_all("div", class_="box_head")
        last_box_head = box_head[-1]
        span_tags = last_box_head.find("span", class_="time")
        days = span_tags.text.strip()
        game_dates = [days[1:-1]] * len(vsbox_list[5:])

        for vsbox in vsbox_list[5:]:
            home_team_element = vsbox.find("p", style="text-align:left;width: 7rem;")
            home_team = home_team_element.find("a").text.strip()

            away_team_element = vsbox.find("p", style="text-align:right;width: 7rem;")
            away_team = away_team_element.find("a").text.strip()

            stadium_element = vsbox.find("span", style="background-color:#EFEFEF;border-radius:3px;line-height:26px;")
            stadium = stadium_element.find("a").text.strip()

            home_teams.append(home_team)
            away_teams.append(away_team)
            stadiums.append(stadium)

        return home_teams, away_teams, stadiums, schedule_times, game_dates
    
    def create_excel_file(self, home_teams, away_teams, stadiums, schedule_times, game_dates):
        df = pd.DataFrame({
            "Date" : game_dates,
            "Home Team": home_teams,
            "Away Team": away_teams,
            "Stadium": stadiums,
            "Schedule Time": schedule_times
        })

        folder_name = 'today_game'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_name = f'{datetime.now().strftime("%Y.%m.%d")}_오늘 경기 일정.xlsx'
        file_path = os.path.join(os.getcwd(), folder_name, file_name)

        try:
            if os.path.exists(file_path):
                raise FileExistsError(f"파일 '{file_path}'은(는) 이미 존재합니다.")

            super().save_to_excel(df, file_path)

        except FileExistsError as e:
            print(f"오류: {e}")

        except Exception as e:
            print(f"예외 발생: {e}")

    def run(self) -> List[T_Game]:
        home_teams, away_teams, stadiums, schedule_times, game_dates = self.scrape_data()
        return T_Game.create_games(home_teams, away_teams, stadiums, schedule_times, game_dates)
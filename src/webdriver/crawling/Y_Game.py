import os
import pandas as pd
import requests
from Scraper import Scraper
from bs4 import BeautifulSoup
from datetime import datetime

class GameResultsScraper(Scraper):
    def __init__(self, url):
        super().__init__(url)

    def scrape_data(self):
        game_results = []
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for g_schedule in soup.find_all("div", class_="g_schedule"):
            for vsbox in g_schedule.find_all("div", class_="vsbox"):
                game_date = vsbox.find("span").text.strip()
                team_scores = vsbox.find_all("p")
                
                team_1_info = team_scores[0].text.strip()
                team_2_info = team_scores[1].text.strip()

                if ' ' not in team_1_info or ' ' not in team_2_info:
                    continue
                
                team_1_name = team_1_info.split(" ")[-2]
                team_1_score = team_1_info.split(" ")[-1]
                team_2_name = team_2_info.split(" ")[0]
                team_2_score = team_2_info.split(" ")[1]

                game_results.append([game_date, team_1_name, team_1_score, team_2_name, team_2_score])

        return game_results

    def scrape_and_save(self, file_name_prefix):
        game_results = self.scrape_data()
        
        game_date = game_results[0][0]
        game_year = datetime.now().year
        full_game_date = f'{game_year}.{game_date}'
        
        df_games = pd.DataFrame(game_results, columns=['Date', 'Team 1', 'Score 1', 'Score 2', 'Team 2'])
        file_path = f'{full_game_date}_{file_name_prefix}.xlsx'
        
        try:
            if os.path.exists(file_path):
                raise FileExistsError(f"파일 '{file_path}'은(는) 이미 존재합니다.")

            self.save_to_excel(df_games, file_path)
        
        except FileExistsError as e:
            print(f"오류: {e}")

        except Exception as e:
            print(f"예외 발생: {e}")

        return file_path

    def save_to_excel(self, df, file_name):
        super().save_to_excel(df, file_name)

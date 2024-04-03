import requests
from Scraper import Scraper
from bs4 import BeautifulSoup
from domain.BoxScore import BoxScore
from typing import List

class BoxScoreScraper(Scraper):
    s_no = 20240041

    def __init__(self):
        self.base_url = "https://statiz.sporki.com/schedule/?m=summary"
        self.game_results = []

    def scrape_data(self):
        for _ in range(5):  # 5번의 데이터를 수집
            current_url = f"{self.base_url}&s_no={BoxScoreScraper.s_no}"
            response = requests.get(current_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            div_sh_box = soup.find("div", class_="sh_box")
            
            if div_sh_box:
                game_date = div_sh_box.find("div", class_="box_head").text.strip().split(' ')[0]
                game_table = div_sh_box.find("table")

                for row in game_table.find_all("tr")[1:]:  # 헤더 제외
                    columns = row.find_all("td")
                    team_name = columns[0].text.strip()
                    inning_scores = []
                    for col in columns[1:-4]:  # R, H, E, B 컬럼을 제외하고 이닝 점수만 추출
                        col_text = col.get_text(strip=True, separator=" ").split()  # 공백을 기준으로 텍스트 분리
                        if col_text:  # 점수가 있는 경우에만 리스트에 추가
                            score = col_text[0]
                            inning_scores.append(score)

                    runs = columns[-4].text.strip()
                    hits = columns[-3].text.strip()
                    errors = columns[-2].text.strip()
                    bases = columns[-1].text.strip()

                    self.game_results.append([game_date, team_name] + inning_scores + [runs, hits, errors, bases])

            BoxScoreScraper.s_no += 1  # 다음 게임 번호로 업데이트

        return self.game_results

    def run(self) -> List[BoxScore]:
        game_results = self.scrape_data()
        return BoxScore.create_box_scores(game_results)
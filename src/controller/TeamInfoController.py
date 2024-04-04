from webdriver.crawling.NewsCrawler import NewsCrawler
from webdriver.crawling.ScoreBoxCrawler import Boxscore

class TeamInfoController:

    @staticmethod
    def get_team_info(teams: list[str]):
        result = dict()
        team_news = NewsCrawler.of(teams).run()
        team_score = Boxscore.of().run()

        for team in teams:
            result[team] = TeamInfoController.find_team(team, team_news, team_score)
        
        return result

    @staticmethod
    def find_team(team, team_news_list, team_scores):
        result = dict()

        for team_score in team_scores:
            if team_score.find_team(team):
                result['team_score'] = team_score
                break

        
        result['team_news'] = []

        for team_news in team_news_list:
            if team_news.getTeam() == team:
                result['team_news'].append(team_news)

        return result
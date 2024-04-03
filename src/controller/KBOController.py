from utils.Mail import Mail
from controller.PlayerController import PlayerController
from utils.HTMLChanger import to_HTML
from controller.NewsController import NewsContoller
from controller.MatchController import MatchController

class KBOController:
    def __init__(self, settings) -> None:
        self.__settings = settings

    def run(self) -> str:
        email = self.__settings['email']
        mail = Mail(email['email'], email['passwd'])

        data = dict()

        data['team_info'] = dict()
        data['ranking_info'] = dict()

        for result in self.__settings['team']['result']:
            data['team_info'][result] = self.select_result(result)

        for rank in self.__settings['rank']:
            data['ranking_info'][rank] = self.select_rank(rank)

        html = to_HTML(data)

        mail.send(html)

    def select_result(self, result_type: str) -> list[object]:
        if result_type == 'recent_match_info':
            return MatchController.get_recent_match_info()
        if result_type == 'today_match_info':
            return MatchController.get_next_match_info()
        if result_type == 'recent_match_news':
            return NewsContoller.get_team_news(self.__settings['team']['teams'])

    def select_rank(self, rank_type: str) -> list[object]:
        if rank_type == 'team_rank':
            return []
        if rank_type == 'players_rank':
            return PlayerController.get_ranking_players()
        
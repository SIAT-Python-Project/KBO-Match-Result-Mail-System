from utils.Mail import Mail
from controller.PlayerController import PlayerController

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

        return self.to_HTML(data)

    def select_result(self, result_type: str) -> list[object]:
        if result_type == 'yester_info':
            return 
        if result_type == 'today_info':
            return 
        if result_type == 'yesterday_news':
            return

    def select_rank(self, rank_type: str) -> list[object]:
        if rank_type == 'team_rank':
            return 
        if rank_type == 'players_rank':
            return PlayerController.get_ranking_players()
        

    def to_HTML(self, data):
        pass

    def to_HTML_team_info(self, data):
        pass

    def to_HTML_recent_match(self, data):
        pass

    def to_HTML_today_match(self, data):
        pass

    def to_HTML_recent_match_news(self, data):
        pass
        
        
        

from utils.Mail import Mail
from controller.PlayerController import PlayerController

class KBOController:
    def __init__(self, settings) -> None:
        self.__settings = settings

    def run(self):
        email = self.__settings['email']
        mail = Mail(email['email'], email['passwd'])

        data = dict()

        data['ranking_info'] = dict()

        for rank in self.__settings['rank']:
            data['ranking_info'][rank] = self.select_rank(rank)

        print(data)

    def select_rank(self, rank_type):
        if rank_type == 'team_rank':
            return 
        if rank_type == 'players_rank':
            return PlayerController.get_ranking_players()
        
        


class Y_Game:
    def __init__(self, game_date: str, team_1_name: str, team_1_score: int, team_2_name: str, team_2_score: int) -> None:
        self.__game_date = game_date
        self.__team_1_name = team_1_name
        self.__team_1_score = team_1_score
        self.__team_2_name = team_2_name
        self.__team_2_score = team_2_score
    
    @staticmethod
    def of(game_info: list) -> "Y_Game":
        game_date, team_1_name, team_1_score, team_2_name, team_2_score = game_info
        return Y_Game(game_date, team_1_name, int(team_1_score), team_2_name, int(team_2_score))

    @classmethod
    def create_games_from_results(cls, game_results: list):
        games = []
        for game_result in game_results:
            game_date, team_1_name, team_1_score, team_2_name, team_2_score = game_result
            games.append(cls(game_date, team_1_name, int(team_1_score), team_2_name, int(team_2_score)))
        return games

    def __str__(self) -> str:
        return f'{self.__game_date}: {self.__team_1_name} {self.__team_1_score} vs {self.__team_2_score} {self.__team_2_name}'
    
    def get_game_date(self):
        return self.__game_date

    def get_team_1_name(self):
        return self.__team_1_name

    def get_team_1_score(self):
        return self.__team_1_score

    def get_team_2_name(self):
        return self.__team_2_name

    def get_team_2_score(self):
        return self.__team_2_score
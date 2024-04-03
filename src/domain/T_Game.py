class T_Game:
    def __init__(self, home_team: str, away_team: str, stadium: str, schedule_time: str, game_date: str) -> None:
        self.__home_team = home_team
        self.__away_team = away_team
        self.__stadium = stadium
        self.__schedule_time = schedule_time
        self.__game_date = game_date

    @staticmethod
    def of(date: str, home_team: str, away_team: str, stadium: str, schedule_time: str) -> "T_Game":
        return T_Game(date, home_team, away_team, stadium, schedule_time)
    
    @classmethod
    def create_games(cls, home_teams: list[str], away_teams: list[str], stadiums: list[str], schedule_times: list[str], game_dates: list[str]):
        games = []
        for home_team, away_team, stadium, schedule_time, game_date in zip(home_teams, away_teams, stadiums, schedule_times, game_dates):
            games.append(cls(home_team, away_team, stadium, schedule_time, game_date))
        return games

    def __str__(self) -> str:
        return f'{self.__date}: {self.__home_team} vs {self.__away_team} at {self.__stadium}, {self.__schedule_time}'

    def toHTML(self):
        html = \
f"""
    <tr>
        <td>{self.__game_date}</td>
        <td>{self.__home_team}</td>
        <td>{self.__away_team}</td>
        <td>{self.__stadium}</td>
        <td>{self.__schedule_time}</td>
    </tr>
"""
        return html

    def get_home_team(self):
        return self.__home_team

    def get_away_team(self):
        return self.__away_team

    def get_stadium(self):
        return self.__stadium

    def get_schedule_time(self):
        return self.__schedule_time
    
    def get_game_date(self):
        return self.__game_date
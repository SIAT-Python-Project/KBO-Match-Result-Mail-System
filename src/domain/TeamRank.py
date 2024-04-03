class TeamRank:
    def __init__(self,team_rank_list) -> None:
        self.__team_rank_list = team_rank_list
        
    def of(team_rank_list):
        return TeamRank(team_rank_list)
    
    def __str__(self) -> str:
        return f'팀순위: {self.__team_rank_list}'
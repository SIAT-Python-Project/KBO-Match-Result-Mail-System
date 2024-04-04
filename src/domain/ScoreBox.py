class GameResult:
    def __init__(self, game_result1) -> None:
        self.__game_result = game_result1
        
    def of(game_result1):
        return GameResult(game_result1)
    
    def __str__(self) -> str:
        return f'팀순위: {self.__game_result}'
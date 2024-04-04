class GameResult:
    def __init__(self, game_result1) -> None:
        self.__game_result = game_result1
    
    def of(game_result1):
        return GameResult(game_result1)
    
    def __str__(self) -> str:
        return f'팀순위: {self.__game_result}'
    
    def toHTML(self) -> str:
        html = '<tr>'

        for data in self.__game_result[1].split():
            html += f'<td>{data}</td>'

        html += '</tr>'
        html += '<tr>'

        for data in self.__game_result[2].split():
            html += f'<td>{data}</td>'

        
        html += '</tr>'



        return html
    
    def find_team(self, target_name) -> bool:
        for score in self.__game_result:
            name = score.split()[0]
            if name == target_name:
                return True
            
        return False
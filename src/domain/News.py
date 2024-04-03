class News:
    def __init__(self, teams, news_title, news_link) -> None:
        self.__news_title = news_title,
        self.__news_link = news_link,
        self.__news_team = teams
        
    @staticmethod
    def of(teams, news_title, news_link) -> object:
        
        return News(teams, news_title, news_link)
    
    def __str__(self) -> str:
        return f'team: {self.__news_team}, news_title: {self.__news_title}, news_link: {self.__news_link}'
        
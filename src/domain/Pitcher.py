class Pitcher:
    def __init__(self, name: str, team: str, earnedRunsAverage: float, win: int, strikeOuts: int) -> None:
        self.__name = name
        self.__team = team
        self.__earnedRunsAverage = earnedRunsAverage
        self.__win = win
        self.__strikeOuts = strikeOuts


    def __str__(self) -> str:
        return f'{self.__name}-{self.__team}: {self.__win} win!, {self.__strikeOuts} SO!!'
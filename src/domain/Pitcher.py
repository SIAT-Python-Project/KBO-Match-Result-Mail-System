class Pitcher:
    def __init__(self, name: str, team: str, earnedRunsAverage: float, win: int, strikeOuts: int) -> None:
        self.__name = name
        self.__team = team
        self.__earnedRunsAverage = earnedRunsAverage
        self.__win = win
        self.__strikeOuts = strikeOuts

    @staticmethod
    def of(name: str, team: str, earnedRunsAverage: float, win: int, strikeOuts: int):
        earnedRunsAverage = float(earnedRunsAverage)
        win = int(win)
        strikeOuts = int(strikeOuts)

        return Pitcher(name, team, earnedRunsAverage, win, strikeOuts)


    def __str__(self) -> str:
        return f'{self.__name}-{self.__team}: {self.__win} win!, {self.__strikeOuts} SO!!'
class Hitter:

    def __init__(self, name: str, team: str, avg: float, hit: int, homeRun: int, runBattedIn: int, stolenBase: int) -> None:
        self.__name = name
        self.__team = team
        self.__avg = avg
        self.__hit = hit
        self.__homeRun = homeRun
        self.__runBattedIn = runBattedIn
        self.__stolenBase = stolenBase

    @staticmethod
    def of(name: str, team: str, avg: float, hit: int, homeRun: int, runBattedIn: int, stolenBase: int) -> object:
        if avg == '-':
            avg = None
        else:
            avg = float(avg)
        hit = int(hit)
        homeRun = int(homeRun)
        runBattedIn = int(runBattedIn)
        stolenBase = int(stolenBase)

        return Hitter(name, team, avg, hit, homeRun, runBattedIn, stolenBase)

    def __str__(self) -> str:
        return f'{self.__name}-{self.__team}: {self.__hit} hit!, {self.__homeRun} Home Run!!'
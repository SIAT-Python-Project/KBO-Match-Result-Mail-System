class Hitter:

    def __init__(self, name: str, team: str, avg: float, PA:int, hit: int, homeRun: int, runBattedIn: int, stolenBase: int) -> None:
        self.__name = name
        self.__team = team
        self.__avg = avg
        self.__PA = PA
        self.__hit = hit
        self.__homeRun = homeRun
        self.__runBattedIn = runBattedIn
        self.__stolenBase = stolenBase

    @staticmethod
    def of(name: str, team: str, avg: float, PA: int, hit: int, homeRun: int, runBattedIn: int, stolenBase: int) -> object:
        if avg == '-':
            avg = None
        else:
            avg = float(avg)
        PA = int(PA)
        hit = int(hit)
        homeRun = int(homeRun)
        runBattedIn = int(runBattedIn)
        stolenBase = int(stolenBase)

        return Hitter(name, team, avg, PA, hit, homeRun, runBattedIn, stolenBase)

    def __str__(self) -> str:
        return f'{self.__name}-{self.__team}: {self.__avg} avg, {self.__hit} hit!, {self.__homeRun} Home Run!!'
    
    def getAvg(self):
        return self.__avg or 0
    
    def getHit(self):
        return self.__hit
    
    def getHomeRun(self):
        return self.__homeRun
    
    def getRunBattedIn(self):
        return self.__runBattedIn
    
    def getStolenBase(self):
        return self.__stolenBase
    
    def getPA(self):
        return self.__PA
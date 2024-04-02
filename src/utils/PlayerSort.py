import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from domain.Hitter import Hitter
from domain.Pitcher import Pitcher
from webdriver.crawling.PitcherCrawler import PitcherCrawler

def sort_hitter_avg(hitter):
    if hitter.getPA() < 20:
        return -1
    else:
        return hitter.getAvg()

def hitter_sort(hitters: list[Hitter], option: str, reverseType: bool=True, count: int=5):
    count = min(len(hitters), count)

    if option == 'AVG':
        return sorted(hitters, key=sort_hitter_avg, reverse=reverseType)[:count]
    if option == 'H':
        return sorted(hitters, key=Hitter.getHit, reverse=reverseType)[:count]
    if option == 'HR':
        return sorted(hitters, key=Hitter.getHomeRun, reverse=reverseType)[:count]
    if option == 'RBI':
        return sorted(hitters, key=Hitter.getRunBattedIn, reverse=reverseType)[:count]
    if option == 'SB':
        return sorted(hitters, key=Hitter.getStolenBase, reverse=reverseType)[:count]
    
    return hitters

def pitcher_sort(pitchers: list[Pitcher], option: str, reverseType: bool=True, count: int=5):
    count = min(len(pitchers), count)

    if option == 'AVG':
        return sorted(pitchers, key=Pitcher.getEarnedRunsAverage, reverse=(not reverseType))[:count]
    if option == 'W':
        return sorted(pitchers, key=Pitcher.getWin, reverse=reverseType)[:count]
    if option == 'SO':
        return sorted(pitchers, key=Pitcher.getStrikeOuts, reverse=reverseType)[:count]
    
    return pitchers
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from domain.Hitter import Hitter

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
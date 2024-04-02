from webdriver.crawling.HitterCrawler import HitterCrawler
from webdriver.crawling.PitcherCrawler import PitcherCrawler
from utils.PlayerSort import *

class PlayerController:

    @staticmethod
    def get_ranking_players():
        players = dict()
        players['hitter'] = PlayerController.get_ranking_hitter()
        players['pitcher'] = PlayerController.get_ranking_pitcher()

        return players

    @staticmethod
    def get_ranking_pitcher():
        pitcher_crawle = PitcherCrawler.of()
        pitchers = pitcher_crawle.run()
        results = dict()

        results['AVG'] = pitcher_sort(pitchers, 'AVG')
        results['W'] = pitcher_sort(pitchers, 'W')
        results['SO'] = pitcher_sort(pitchers, 'SO')

        return results

    @staticmethod
    def get_ranking_hitter():
        hitter_crawle = HitterCrawler.of()
        hitters = hitter_crawle.run()
        results = dict()

        results['AVG'] = hitter_sort(hitters, 'AVG')
        results['H'] = hitter_sort(hitters, 'H')
        results['HR'] = hitter_sort(hitters, 'HR')
        results['RBI'] = hitter_sort(hitters, 'RBI')
        results['SB'] = hitter_sort(hitters, 'SB')

        return results
        
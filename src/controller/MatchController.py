from webdriver.crawling.Y_GameCrawler import GameResultsScraper
from webdriver.crawling.T_GameCrawler import GameInfoScraper

class MatchController:

    @staticmethod
    def get_recent_match_info():
        scraper = GameResultsScraper('https://statiz.sporki.com/')
        datas = scraper.run()
        
        return datas
    
    @staticmethod
    def get_next_match_info():
        scraper = GameInfoScraper('https://statiz.sporki.com/')
        datas = scraper.run()
        return datas
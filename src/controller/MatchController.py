from webdriver.crawling.Y_GameCrawler import GameResultsScraper as YS
from webdriver.crawling.T_GameCrawler import GameInfoScraper as NS

class MatchController:

    @staticmethod
    def get_recent_match_info():
        scraper = YS('https://statiz.sporki.com/')
        datas = scraper.run()
        
        return datas
    
    @staticmethod
    def get_next_match_info():
        scraper = NS('https://statiz.sporki.com/')
        datas = scraper.run()
        return datas
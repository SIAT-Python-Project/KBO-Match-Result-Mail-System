from webdriver.crawling.NewsCrawler import NewsCrawler

class NewsContoller:

    @staticmethod
    def get_team_news(teams: list[str]):
        datas = NewsCrawler.of(teams).run()

        result = dict()

        for data in datas:
            team = data.getTeam()

            if team in result:
                result[team].append(data)
            else:
                result[team] = [data]

        return result
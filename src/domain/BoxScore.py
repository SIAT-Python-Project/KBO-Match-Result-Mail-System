class BoxScore:
    def __init__(self, game_date: str, team_name: str, inning_scores: list[int], runs: int, hits: int, errors: int, bases: int) -> None:
        self.__game_date = game_date
        self.__team_name = team_name
        self.__inning_scores = inning_scores
        self.__runs = runs
        self.__hits = hits
        self.__errors = errors
        self.__bases = bases

    @staticmethod
    def of(game_info: list) -> "BoxScore":
        game_date, team_name, *inning_scores, runs, hits, errors, bases = game_info
        inning_scores_int = [int(score) for score in inning_scores]
        return BoxScore(game_date, team_name, inning_scores_int, int(runs), int(hits), int(errors), int(bases))

    @classmethod
    def create_box_scores(cls, game_results: list):
        box_scores = []
        for game_result in game_results:
            box_score = cls.of(game_result)
            box_scores.append(box_score)
        return box_scores

    def __str__(self) -> str:
        return f'{self.__game_date}: {self.__team_name} - Runs: {self.__runs}, Hits: {self.__hits}, Errors: {self.__errors}, Bases: {self.__bases}'

    def get_game_date(self):
        return self.__game_date

    def get_team_name(self):
        return self.__team_name

    def get_inning_scores(self):
        return self.__inning_scores

    def get_runs(self):
        return self.__runs

    def get_hits(self):
        return self.__hits

    def get_errors(self):
        return self.__errors

    def get_bases(self):
        return self.__bases
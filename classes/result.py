from classes.solution import Solution


class Result:
    def __init__(self, objetivo, results: list(Solution)):
        self.objetivo = objetivo
        self.result = results
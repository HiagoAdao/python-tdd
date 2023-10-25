class Game:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def pontuar(self, score):
        self.total_score += score

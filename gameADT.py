class GameADT:
    def __init__(self, name):
        self.name = name
        self.pts = []

    @property
    def total_score(self):
        return sum(self.pts)

    def pontuar(self, score):
        self.pts.append(score)

class Score:

    def __init__(self):
        self.score_player = 0
        self.score_comp = 0

    def in_scorep(self):
        self.score_player += 1
        return self.score_player

    def in_scorec(self):
        self.score_comp += 1
        return self.score_comp

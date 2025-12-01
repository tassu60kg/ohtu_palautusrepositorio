class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def equal_score(self):
        if self.player1_score == 0:
            return "Love-All"
        if self.player1_score == 1:
            return "Fifteen-All"
        if self.player1_score == 2:
            return "Thirty-All"
        return "Deuce"

    def find_advantage(self, difference):
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def uneven_scores(self,score_str):
        score = 0
        score = self.player1_score
        score_str = self.convert_score(score,score_str)
        score_str = score_str + "-"
        score = self.player2_score
        score_str = self.convert_score(score,score_str)
        return score_str

    def convert_score(self,score,score_str):
        if score == 0:
            return score_str + "Love"
        elif score == 1:
            return score_str + "Fifteen"
        elif score == 2:
            return score_str + "Thirty"
        elif score == 3:
            return score_str + "Forty"

    def get_score(self):
        score_str = ""

        if self.player1_score == self.player2_score:
            score_str = self.equal_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score_str = self.find_advantage(self.player1_score - self. player2_score)
        else:
            score_str = self.uneven_scores(score_str)
        return score_str

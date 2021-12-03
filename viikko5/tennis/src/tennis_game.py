class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self.even()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.advantage()
        else:
            score = self.player_score(self.m_score1)+"-"+self.player_score(self.m_score2)
        return score

    def even(self):
        if self.m_score1 == 0:
            score = "Love-All"
        elif self.m_score1 == 1:
            score = "Fifteen-All"
        elif self.m_score1 == 2:
            score = "Thirty-All"
        elif self.m_score1 == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        
        return score

    def advantage(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score

    def player_score(self, points):
        if points == 0:
            score = "Love"
        elif points == 1:
            score = "Fifteen"
        elif points == 2:
            score = "Thirty"
        elif points == 3:
            score = "Forty"

        return score
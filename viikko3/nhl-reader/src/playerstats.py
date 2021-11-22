from playerreader import PlayerReader

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.players
        top_scorers = []

        for player in players:
            if player.nationality == nationality:
                top_scorers.append(player)

        top_scorers.sort(key = lambda x: x.goals + x.assists, reverse=True)

        return top_scorers
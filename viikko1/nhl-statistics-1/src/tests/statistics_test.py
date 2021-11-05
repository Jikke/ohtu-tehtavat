import statistics
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_konstuktori_toimii_oikein(self):
        constructed = self.statistics._players
        kurri = Player("Kurri",   "EDM", 37, 53)

        self.assertEqual(constructed[2].name, kurri.name)

    def test_tehot_lasketaan_oikein(self):
        player = Player("Kurri",   "EDM", 37, 53)
        actual = 37+53
        points = statistics.sort_by_points(player)

        self.assertEqual(points, actual)

    def test_pelaajahaku_löytää_oikein(self):
        found = self.statistics.search("Kurri")
        kurri = Player("Kurri",   "EDM", 37, 53)

        self.assertEqual(found.name, kurri.name)

    def test_pelaajahaku_ei_löydä_oikein(self):
        found = self.statistics.search("Virtanen")

        self.assertEqual(found, None)

    def test_joukkuehaku_löytää_oikein(self):
        team = self.statistics.team("EDM")
        actual = [Player("Semenko", "EDM", 4, 12), Player("Kurri",   "EDM", 37, 53), Player("Gretzky", "EDM", 35, 89)]

        self.assertEqual(team[1].name, actual[1].name)

    def test_huippuhaku_löytää_oikein(self):
        top = self.statistics.top_scorers(2)

        self.assertEqual(top[1].name, "Lemieux")
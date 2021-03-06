import unittest
import numpy as np

from game_play import *
from game import *
from player import *


class TestGamePlay(unittest.TestCase):

    def setUp(self):
        self.player1 = Player([0])
        self.player2 = Player([1])
        self.pd = Game(np.array([[2, 0], [4, 1]]))
        self.subject = GamePlay(self.player1, self.player2, self.pd)

    def test_getPlayer_ReturnsPlayerInstance_givenPlayer1Or2(self):
        self.assertIsInstance(self.subject.players[0], Player)
        self.assertIsInstance(self.subject.players[1], Player)

    def test_game_ReturnsGameInstance(self):
        self.assertIsInstance(self.subject.game, Game)

    def test_getGame_ReturnsSpecGameInstance_givenSpecGame(self):
        self.assertEqual(self.subject.game, self.pd)

    def test_returnPlayerPayoffs_returnsProperPdPayoffs(self):
        payoffs04 = self.subject.returnPlayerPayoffs(0, 1)
        self.assertEqual(payoffs04, (0, 4))

        payoffs11 = self.subject.returnPlayerPayoffs(1, 1)
        self.assertEqual(payoffs11, (1, 1))

        payoffs22 = self.subject.returnPlayerPayoffs(0, 0)
        self.assertEqual(payoffs22, (2, 2))

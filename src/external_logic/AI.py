from random import randint

from src.external_logic.Player import Player
from src.internal_logic.Dot import Dot


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d

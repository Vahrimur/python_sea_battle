from src.exceptions.BoardException import BoardException


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):  # получение координат для выстрела
        raise NotImplementedError()

    def move(self):  # ход игрока
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

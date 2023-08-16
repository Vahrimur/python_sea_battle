from random import randint

from src.exceptions.BoardException import BoardWrongShipException
from src.external_logic.AI import AI
from src.external_logic.User import User
from src.internal_logic.Board import Board
from src.internal_logic.Dot import Dot
from src.internal_logic.Ship import Ship


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):  # получение доски со случайно расставленными кораблями для игры
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):  # составление доски со случайно расставленными кораблями
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):  # вывод приветствия в начале игры
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):  # процесс игры до чьего-нибудь выигрыша
        try:
            num = 0
            while True:
                print("-" * 20)
                print("Доска пользователя:")
                print(self.us.board)
                print("-" * 20)
                print("Доска компьютера:")
                print(self.ai.board)
                if num % 2 == 0:
                    print("-" * 20)
                    print("Ходит пользователь!")
                    repeat = self.us.move()
                else:
                    print("-" * 20)
                    print("Ходит компьютер!")
                    repeat = self.ai.move()
                if repeat:
                    num -= 1

                if self.ai.board.count == 7:
                    print("-" * 20)
                    print("Пользователь выиграл!")
                    break

                if self.us.board.count == 7:
                    print("-" * 20)
                    print("Компьютер выиграл!")
                    break
                num += 1
        except KeyboardInterrupt:
            print("\nИгра прервана. Сыграем еще раз?")

    def start(self):
        self.greet()
        self.loop()

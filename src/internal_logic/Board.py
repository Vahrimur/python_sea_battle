from src.exceptions.BoardException import BoardWrongShipException, BoardOutException, BoardUsedException
from src.internal_logic.Dot import Dot


class Board:

    def __init__(self, hid=False, size=6):
        self.size = size  # длина стороны доски
        self.hid = hid  # режим отображения кораблей на доске

        self.count = 0  # количество пораженных кораблей

        self.field = [["O"] * size for _ in range(size)]  # поле из клеток, в которых храним текущие состояния

        self.busy = []  # занятые точки
        self.ships = []  # список кораблей

    def add_ship(self, ship):  # добавление корябля на доску
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):  # добавление контура вокруг корабля
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def __str__(self):  # отображение игровой доски
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, d):  # проверка попадания точки вне игровой доски
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):  # выстрел по заданным координатам
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return True
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "T"
        print("Мимо!")
        return False

    def begin(self):  # обнуление списка занятых точек
        self.busy = []

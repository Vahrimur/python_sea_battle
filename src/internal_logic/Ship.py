from src.internal_logic.Dot import Dot


class Ship:

    def __init__(self, bow, l, o):
        self.bow = bow  # координаты носа корабля
        self.l = l  # длина корабля
        self.o = o  # ориентация корабля на игровой доске
        self.lives = l  # количество жизней корабля

    @property
    def dots(self):  # получение списка точек корабля
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:  # вертикальная ориентация
                cur_x += i

            elif self.o == 1:  # горизонтальная ориентация
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):  # проверка попадания по кораблю
        return shot in self.dots

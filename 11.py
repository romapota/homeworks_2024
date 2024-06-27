import random

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * length
    def set_start_coords(self, x, y):
        self._x = x
        self._y = y
    def get_start_coords(self):
        return self._x, self._y
    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go
    def is_collide(self, ship):
        for i in range(self._length):
            for j in range(ship._length):
                dx = (self._x + i if self._tp == 1 else self._x) - (ship._x + j if ship._tp == 1 else ship._x)
                dy = (self._y + i if self._tp == 2 else self._y) - (ship._y + j if ship._tp == 2 else ship._y)
                if abs(dx) <= 1 and abs(dy) <= 1:
                    return True
        return False
    def is_out_pole(self, size):
        if self._tp == 1:
            return not (0 <= self._x < size and 0 <= self._y < size and self._x + self._length - 1 < size)
        else:
            return not (0 <= self._x < size and 0 <= self._y < size and self._y + self._length - 1 < size)
    def __getitem__(self, index):
        return self._cells[index]
    def __setitem__(self, index, value):
        self._cells[index] = value
        if value == 2:
            self._is_move = False

class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
    def init(self):
        ship_sizes = [4, 3, 3, 2, 2, 1, 1, 1, 1]
        for size in ship_sizes:
            ship = Ship(size, tp=random.randint(1, 2))
            placed = False
            while not placed:
                x, y = random.randint(0, self._size - 1), random.randint(0, self._size - 1)
                ship.set_start_coords(x, y)
                if self._can_place(ship):
                    placed = True
                    self._ships.append(ship)
    def _can_place(self, ship):
        for other_ship in self._ships:
            if ship.is_collide(other_ship) or ship.is_out_pole(self._size):
                return False
        return True
    def get_ships(self):
        return self._ships
    def move_ships(self):
        for ship in self._ships:
            direction = random.choice([-1, 1])
            ship.move(direction)
            if ship.is_out_pole(self._size) or any(ship.is_collide(other) for other in self._ships if other != ship):
                ship.move(-direction)
                if ship.is_out_pole(self._size) or any(ship.is_collide(other) for other in self._ships if other != ship):
                    ship.move(direction)
    def show(self):
        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            for i in range(ship._length):
                if ship._tp == 1:
                    pole[y][x + i] = ship[i]
                else:
                    pole[y + i][x] = ship[i]
        for row in pole:
            print(' '.join(str(cell) for cell in row))
    def get_pole(self):
        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            for i in range(ship._length):
                if ship._tp == 1:
                    pole[y][x + i] = ship[i]
                else:
                    pole[y + i][x] = ship[i]
        return tuple(tuple(row) for row in pole)
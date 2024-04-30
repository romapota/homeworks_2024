@singltone
class GamePole:
    def __init__(self, N, M, total_mines):
        self.__pole_cells = tuple()
        self.N = N
        self.M = M
        self.total_mines = total_mines
    def init_pole(self):
        pass
    def open_celi(self, i, j):
        pass
    def show_pole(self):
        pass
class Cell:
    def __init__(self):
        self.__is_mine = None
        self.__number = None
        self.__is_open = False
    #property
print(bool(Cell))
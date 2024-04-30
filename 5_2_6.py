import random

class GamePole:
    @property
    def pole(self):
        return self.__pole_cells
    @pole.getter
    def pole(self):
        return self.__pole_cells
    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for i in range(self.M)] for i in range(self.N)]
        self.game_over = False
    def init_pole(self):
        self.count = self.total_mines
        while self.count != 0:
            for i in range(self.N):
                for j in range(self.M):
                    choose = random.randint(0, 30)
                    if choose == 2 and self.count > 0 and self.pole[i][j].is_mine == False:
                        self.pole[i][j].is_main = True
                        self.count -= 1
        for i in range(self.N):
            for j in range(self.M):
                count = 0
                try:
                    if self.pole[i][j-1].is_mine:
                        count += 1
                except: pass
                try:
                    if self.pole[i][j+1].is_mine:
                        count += 1
                except: pass
                try:
                    if self.pole[i+1][j].is_mine:
                        count += 1
                except: pass
                try:
                    if self.pole[i-1][j].is_mine:
                        count += 1
                except: pass
                try:
                    if self.pole[i-1][j-1].is_mine:
                        count += 1
                except: pass
                try:
                    if self.pole[i-1][j+1].is_mine:
                        count += 1
                except: pass
                try:
                    if self.pole[i+1][j+1].is_mine:
                        count += 1
                except: pass
                try:
                    if self.pole[i+1][j-1].is_mine:
                        count += 1
                except: pass
                self.pole[i][j].number = count
    def open_cell(self, i, j):#i - строка, j - столбец
        try:
            self.pole[i][j].is_open = True
            if self.pole[i][j].is_mine and self.pole[i][j].is_open:
                self.game_over = True
        except: raise IndexError('некорректные индексы i, j клетки игрового поля')
    def show_pole(self):#N - строка, M - ряд
        if self.game_over == False:
            for i in range(self.N):
                for j in range(self.M):
                    if self.pole[i][j].is_open == False:
                        print('* ', end=" ")
                    if self.pole[i][j].is_open == True and self.pole[i][j].is_mine == False:#клетка открыта и там нет мины
                        print('+ ', end=" ")
                print('\n')
        if self.game_over == True:
            for i in range(self.N):
                for j in range(self.M):
                    if self.pole[i][j].is_mine == False:
                        print('- ', end=" ")
                    if self.pole[i][j].is_mine:#клетка открыта и там нет мины
                        print('! ', end=" ")
                print('\n')
            print('Игра окончена!')

class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = None
        self.__is_open = False
    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_main(self, bools):
        if bools in [True, False]:
            self.__is_mine = bools
        else:
            raise ValueError("недопустимое значение атрибута")
    # @is_main.getter
    # def is_main(self):
    #     return self.__is_mine
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, count):
        if count in [i for i in range(9)]:
            self.__number = count
        else:
            raise ValueError("недопустимое значение атрибута")
    @property
    def is_open(self):
        return self.__is_open
    @is_open.setter
    def is_open(self, bools):
        if bools in [True, False]:
            self.__is_open = bools
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        if self.is_open == False:
            return True
        else:
            return False

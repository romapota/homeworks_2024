import random
class TicTacToe(tuple):
    FREE_CELL = 0 #свободная клетка
    HUMAN_X = 1#крестик(игрок - человек)
    COMPUTER_O = 2#нолик (игрок - компьютер)
    hods = []
    game_over = False
    def __bool__(self):
        if self.game_over == False:
            return True
        else: return False
    def init(self):
        self.lst = [[Cell() for i in range(3)] for i in range(3)]
    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.lst[j][i].value, end=" ")
            print('\n')
    def human_go(self, x, y):

        if self.lst[int(x)][int(y)].value == self.FREE_CELL:
            self.lst[int(x)][int(y)].value = self.HUMAN_X
            self.hods.append([int(x), int(y), 1])
            if self.is_human_win:
                self.game_over = True
                print('Победил человек')
            if self.is_draw:
                self.game_over = True
                print('Ничья')
        else: raise ValueError('клетка уже занята')
    def computer_go(self):
        check = False
        while check == False:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.lst[x][y].value == 0:
                check = True
                self.lst[x][y].value = self.COMPUTER_O
                self.hods.append([x,y,2])
        if self.is_computer_win:
            self.game_over = True
            print('Победил компьютер')
        if self.is_draw:
            self.game_over = True
            print('Ничья')
    def __getitem__(self, item):
        DIGIT = [0, 1, 2]
        if item[0].__class__.__name__ == 'slice':
            return [self.lst[item[1]][i].value for i in range(3)]
        if item[1].__class__.__name__ == 'slice':
            return [self.lst[i][item[0]].value for i in range(3)]
        if item[1] in DIGIT and item[0] in DIGIT:
            try: return self.lst[item[0]][item[1]].value
            except: raise IndexError('неверный индекс клетки')
    def __setitem__(self, key, value):
        pass
    @property
    def is_human_win(self):
        combinate = [[[0,0,1], [0,1,1], [0,2,1]], [[1,0,1], [1,1,1], [1,2,1]], [[2, 0,1], [2, 1,1], [2, 2,1]], [[0, 0,1], [1, 0,1], [2,0,1]], [[0, 1,1], [1, 1,1], [2, 1],1], [[0,2,1], [1, 2,1], [2,2,1]], [[0,0,1], [1,1,1], [2,2,1]], [[0,2,1], [1,1,1], [2, 0,1]]]
        checks = 0
        for i in combinate:
            checks = 0
            for j in i:
                if j in self.hods:
                    checks += 1
                if checks == 3:
                    return True
    @property
    def is_computer_win(self):
        combinate = [[[0, 0, 2], [0, 1, 2], [0, 2, 2]], [[1, 0, 2], [1, 1, 2], [1, 2, 2]], [[2, 0, 2], [2, 1, 2], [2, 2, 2]],
                         [[0, 0, 2], [1, 0, 2], [2, 0, 2]], [[0, 1, 2], [1, 1, 2], [2, 1, 2]], [[0, 2, 2], [1, 2, 2], [2, 2, 2]],
                         [[0, 0, 2], [1, 1, 2], [2, 2, 2]], [[0, 2, 2], [1, 1, 2], [2, 0, 2]]]
        checks = 0
        for i in combinate:
            checks = 0
            for j in i:
                if j in self.hods:
                    checks += 1
                if checks == 3:
                    return True
    @property
    def is_draw(self):
        cells = 9
        for i in range(2):
            for j in range(2):
                if self.lst[i][j].value != 0:
                    cells -= 1
                if cells <= 0:
                    return True
class Cell:
    def __init__(self):
        self.value = 0#0-клетка свободна(поумолчанию), 1-стоит крестик, 2-стоит нолик

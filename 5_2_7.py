
class TicTacToe():
    def __init__(self):
        self.lst = [[Cell() for i in range(3)] for i in range(3)]
    def __getitem__(self, item):
        DIGIT = [0, 1, 2]
        if item[1].__class__.__name__ == 'slice':
            return [self.lst[item[0]][i].value for i in range(3)]
        if item[0].__class__.__name__ == 'slice':
            return [self.lst[i][item[1]].value for i in range(3)]
        if item[1] in DIGIT and item[0] in DIGIT:
            try: return self.lst[item[0]][item[1]].value
            except: raise IndexError('неверный индекс клетки')

    def __setitem__(self, key, value):
                if self.lst[key[0]][key[1]].is_free:
                    try:
                        self.lst[key[0]][key[1]].value = value
                        self.lst[key[0]][key[1]].is_free = False
                    except: raise ValueError('неверный индекс клетки')
                else:
                    raise ValueError('клетка уже занята')
    def clear(self):
        for i in range(3):
            for j in range(3):
                self.lst[i][j].value = 0
                self.lst[i][j].is_free = True
class Cell():
    def __init__(self):
        self.is_free = True
        self.value = 0
    def __bool__(self):
        if self.is_free:
            return True
        else: return False

game = TicTacToe()
game.clear()
print(bool(game[0,0]))
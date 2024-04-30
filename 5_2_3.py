class ListMath():
    def __init__(self, values):
        self.lst_math = []
        for i in values:
            if type(i) != bool and type(i) != str:
                self.lst_math.append(i)
    def __add__(self, other):
        if type(other) == int:
            for i in self.lst_math:
                self.lst_math[i] += other
            return self.lst_math
    def __iadd__(self, other):
        if type(other) == int:
            for i in self.lst_math:
                self.lst_math[i] += other
            return self.lst_math
    def __sub__(self, other):
        for i in self.lst_math:
            self.lst_math[i] -= other
        return self.lst_math
    def __isub__(self, other):
        for i in self.lst_math:
            self.lst_math[i] -= other
        return self.lst_math
    def __imul__(self, other):
        for i in self.lst_math:
            self.lst_math[i] *= other
        return self.lst_math
    def __mul__(self, other):
        for i in self.lst_math:
            self.lst_math[i] *= other
        return self.lst_math
    def __itruediv__(self, other):
        for i in self.lst_math:
            self.lst_math[i] /= other
        return self.lst_math

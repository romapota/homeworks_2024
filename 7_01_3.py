class ListInteger(list):
    def __init__(self, lst):
        check = True
        for i in lst:
            if not isinstance(i, int):
                check = False
                raise TypeError('Можно передавать только целочисленные значения')
        if check:
            super().__init__(lst)
    def __setitem__(self, key, value):
        if isinstance(value, int):
            super().__setitem__(key, value)
        else:
            raise TypeError('Можно передавать только целочисленные значения')
    def append(self, value):
        if isinstance(value, int):
            super().append(value)
        else:
            raise TypeError('Можно передавать только целочисленные значения')
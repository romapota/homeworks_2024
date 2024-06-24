class Furniture():
    def __init__(self, name, weight):
        if self.__verify_name:
            self._name = name
        if self.__verify_weight:
            self._weight = weight

    def __verify_name(self):
        if not isinstance(self._name, str):
            raise TypeError('Название должно быть строкой')
        else:
            return True
    def __verify_weight(self):
        if self._weight < 0:
            raise TypeError('Вес должен быть положительным числом')
        else:
            return True

class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return (self._name, self._weight, self._tp, self._doors)

class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return (self._name, self._weight, self._height)

class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return (self._name, self._weight, self._height, self._square)
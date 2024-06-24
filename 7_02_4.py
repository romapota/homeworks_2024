class Shopinterface():
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(Shopinterface):
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = name.__hash__() + weight.__hash__() + price.__hash__()

    def get_id(self):
        return self.__id
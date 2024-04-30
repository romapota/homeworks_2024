def max_v(i):
    return i[2]


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    def __init__(self, a, b, c):
        if (a >= Dimensions.MIN_DIMENSION or a <= Dimensions.MAX_DIMENSION) and (b >= Dimensions.MIN_DIMENSION or b <= Dimensions.MAX_DIMENSION) and (c >= Dimensions.MIN_DIMENSION or c <= Dimensions.MAX_DIMENSION):
            self._a = a
            self._b = b
            self._c = c
        else:
            raise ValueError("Не правильное значение")
    def __lt__(self, other):
        v1 = self._a * self._b * self._c
        v2 = other._a * other._b * other._c
        return v1 < v2
    def __le__(self, other):
        v1 = self._a * self._b * self._c
        v2 = other._a * other._b * other._c
        return v1 <= v2
    def __gt__(self, other):
        v1 = self._a * self._b * self._c
        v2 = other._a * other._b * other._c
        return v1 > v2
    def __ge__(self, other):
        v1 = self._a * self._b * self._c
        v2 = other._a * other._b * other._c
        return v1 >= v2
class ShopItem:
    lst_shop = []
    def __init__(self, name, price, dims):
        self.name = name
        self.price = price
        self.dim = (dims._a, dims._b, dims._c)
        ShopItem.lst_shop.append([self.name, self.price, (dims._a, dims._b, dims._c)])
        ShopItem.lst_shop_sorted = sorted(ShopItem.lst_shop)

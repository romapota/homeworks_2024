class ShopGenericView:
    def __str__(self):
        for i in self.__dict__:
            return f'{i}:{str(self.__dict__[i])}'

    def __repr__(self):
        return self.__str__

class ShopUserView:
    def __str__(self):
        for i in self.__dict__:
            if str(i) != '_id':
                return f'{i}:{str(self.__dict__[i])}'

    def __repr__(self):
        return self.__str__
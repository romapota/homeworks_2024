class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.__old = old

    @property
    def kind(self):
        return self.__kind
    @kind.setter
    def kind(self, kind):
        self.__kind = kind


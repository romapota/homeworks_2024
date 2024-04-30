class NewList:
    def __init__(self, value):
        self.value = value
    def __sub__(self, other):
        for i in other.value:
            if i in self.value and type(i) != bool:
                print(i)
                self.value.remove(i)
            if i == True and True in self.value:
                self.value.remove(True)
            if i == False and False in self.value:
                self.value.remove(False)
        return self.value
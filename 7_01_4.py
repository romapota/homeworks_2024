class Animal:
    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old
class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: int):
        super().__init__(name, old)
        self.color = color
        self.weight = weight
    def get_info(self):
        s = f'{self.name}: {self.old}, {self.color}, {self.old}'
        return s
class Dog(Animal):
    def __init__(self, name: str, old: int, breed: str, size: int):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
    def get_info(self):
        s = f'{self.name}: {self.old}, {self.breed}, {self.size}'
        return s

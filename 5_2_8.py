class Bag(list):
    def __init__(self, max_weight, *args):
        super().__init__()
        self.max_weight = max_weight
        self.weight = 0
    def add_thing(self, thing):
        if self.weight + thing.weight <= self.max_weight:
            self.weight += thing.weight
            self.append(thing)
        else:
            raise ValueError('превышен суммарный вес предметов')
    def __setitem__(self, key, value):
        if self.weight + value.weight <= self.max_weight:
            self.weight += value.weight
            self.append(value)
        else:
            raise ValueError('превышен суммарный вес предметов')
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
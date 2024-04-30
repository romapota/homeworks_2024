class Recipe:
    def __init__(self):
        self.ings = set()
    def add_ingredient(self, ing):
        self.ings.add(f"{ing.name}: {ing.volume}, {ing.measure}")
    def get_ingredient(self):
        return self.ings
class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

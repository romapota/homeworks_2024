class ShopItem:
    shop_items_lst = []
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        ShopItem.shop_items_lst.append([self.name, self.weight, self.price])
    def __hash__(self):

# shopItems = [ShopItem(f"shopItem_{i}", '2000', '1200') for i in range(5)]
# print(shopItems[1].name)
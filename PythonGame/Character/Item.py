class Item:
    def __init__(self, item_name, weight, price, lvl, stats):
        self.item_name = item_name
        self.item_weight = weight
        self.item_price = price
        self.item_usage_lvl = lvl
        self.item_stats = stats

    def item(self):
        return f"{self.item_name}, {self.item_weight}, {self.item_price}, {self.item_usage_lvl}, {self.item_stats}"

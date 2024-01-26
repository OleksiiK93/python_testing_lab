class Customer:
    def __init__(self, name, wallet, age) -> None:
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = 0
    
    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        if self.wallet >= drink['info'].price:
            self.reduce_wallet(drink['info'].price)
            self.energy += drink['info'].caffeine_level
    
    def buy_food(self, food):
        if self.wallet >= food.price:
            self.reduce_wallet(food.price)
            self.energy -= food.digestion_level
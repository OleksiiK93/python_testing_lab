class Customer:
    def __init__(self, name, wallet, age) -> None:
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = 0
    
    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy(self, drink):
        self.reduce_wallet(drink.price)
        self.energy += drink.caffeine_level
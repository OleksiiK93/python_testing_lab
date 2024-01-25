class Customer:
    def __init__(self, name, wallet, age) -> None:
        self.name = name
        self.wallet = wallet
        self.age = age
    
    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy(self, drink):
        self.reduce_wallet(drink.price)
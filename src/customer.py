class Customer:
    def __init__(self, name, wallet) -> None:
        self.name = name
        self.wallet = wallet
    
    def reduce_wallet(self, amount):
        self.wallet -= amount
class CoffeeShop:
    def __init__(self, name, till, drinks) -> None:
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def sell(self, drink, customer):
        customer.buy(drink)
        self.till += drink.price
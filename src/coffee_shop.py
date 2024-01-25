class CoffeeShop:
    def __init__(self, name, till, drinks) -> None:
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def sell(self, drink, customer):
        if customer.energy <= 100:
            if customer.age > 15 or drink.name == 'Tea':
                customer.buy(drink)
                self.till += drink.price
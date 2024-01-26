class CoffeeShop:
    def __init__(self, name, till, drinks) -> None:
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def sell_drink(self, drink, customer):
        if customer.energy <= 100:
            if customer.age > 15 or drink == self.drinks['tea']:
                customer.buy_drink(drink)
                self.till += drink['info'].price
                drink['amount'] -= 1

    def stock(self):
        stock = {}
        for key, value in self.drinks.items():
            stock[key] = value['amount']
        return stock
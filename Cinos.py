
class Order:
    def __init__(self):
        self.drinks = []
        self.total = 0

    def add_drink(self, base, flavor, price):
        drink = f"{base} with {flavor}"
        self.drinks.append(drink)
        self.total += price

    def get_total(self):
        return self.total

    def get_receipt(self):
        receipt = "Order Receipt:\n"
        for drink in self.drinks:
            receipt += f"- {drink}\n"
        receipt += f"Total: ${self.total:.2f}"
        return receipt

if __name__ == "__main__":
    bases = ['water', 'pokecola', 'sbrite', 'Mr. salt', 'hill fog', 'leaf wine']
    flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
    prices = {'water': 1.0, 'pokecola': 2.5, 'sbrite': 2.0, 'Mr. salt': 1.5, 'hill fog': 3.0, 'leaf wine': 2.75,
              'lemon': 0.5, 'cherry': 0.75, 'strawberry': 0.6, 'mint': 0.4, 'blueberry': 0.8, 'lime': 0.5}

    order = Order()
    from itertools import product

    for base, flavor in product(bases, flavors):
        order.add_drink(base, flavor, prices[base] + prices[flavor])

    print(order.get_receipt())
    



class Order:
    """Represents a drink order containing multiple drinks and their total price.

    The Order class allows adding drinks with specific bases, flavors, and prices,
    and provides methods to retrieve the total price and a formatted receipt.
    """

    def __init__(self):
        """create a new Order with no drinks and a price of zero."""
        self.drinks = []
        self.total = 0

    def add_drink(self, base, flavor, price):
        """Add a drink to the order with the specified base, flavor, and price.

        Arguments for each drink:
            base string: The base of the drink.
            flavor string: The flavor to add to the drink.
            price float: The price of the drink.
        """
        drink = f"{base} with {flavor}"
        self.drinks.append(drink)
        self.total += price

    def get_total(self):
        """Get the total price of the order.

        Returns a float which is the total price of all drinks in the order.
        """
        return self.total

    def get_receipt(self):
        """Create the receipts format.

        Return a string containing the list of drinks and the total price.
        """
        receipt = "Order Receipt:\n"
        for drink in self.drinks:
            receipt += f"- {drink}\n"
        receipt += f"Total: ${self.total:.2f}"
        return receipt

if __name__ == "__main__":
    bases = ['water', 'pokecola', 'sbrite', 'Mr. salt', 'hill fog', 'leaf wine']
    flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime'],
    prices = {'water': 1.0, 'pokecola': 2.5, 'sbrite': 2.0, 'Mr. salt': 1.5, 'hill fog': 3.0, 'leaf wine': 2.75,
              'lemon': 0.5, 'cherry': 0.75, 'strawberry': 0.6, 'mint': 0.4, 'blueberry': 0.8, 'lime': 0.5}

    order = Order()
    from itertools import product

    for base, flavor in product(bases, flavors):
        order.add_drink(base, flavor, prices[base] + prices[flavor])

    print(order.get_receipt())
    



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
    


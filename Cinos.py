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
    foods = {
        'Hotdog': 2.30, 'Corndog': 2.00, 'Ice Cream': 3.00, 'Onion Rings': 1.75,
        'French Fries': 1.50, 'Tater Tots': 1.70, 'Nacho Chips': 1.90
    }
    toppings = {
        'Cherry': 0.00, 'Whipped Cream': 0.00, 'Caramel Sauce': 0.50, 'Chocolate Sauce': 0.50,
        'Nacho Cheese': 0.30, 'Chili': 0.60, 'Bacon Bits': 0.30, 'Ketchup': 0.00, 'Mustard': 0.00
    }
    flavors = {'lemon': 0.15, 'cherry': 0.15, 'strawberry': 0.15, 'mint': 0.15, 'blueberry': 0.15, 'lime': 0.15}
    sizes = {'small': 1.5, 'medium': 1.75, 'large': 2.05, 'mega': 2.15}
    prices = {'water': 1.0, 'pokecola': 2.5, 'sbrite': 2.0, 'Mr. salt': 1.5, 'hill fog': 3.0, 'leaf wine': 2.75,
              'lemon': 0.5, 'cherry': 0.75, 'strawberry': 0.6, 'mint': 0.4, 'blueberry': 0.8, 'lime': 0.5}

    order = Order()
    from itertools import product

    # Add drinks
    for base, flavor in product(bases, flavors):
        order.add_drink(base, flavor, prices[base] + prices[flavor])

    # Add foods with toppings and sizes
    for food, food_price in foods.items():
        for topping, topping_price in toppings.items():
            for size, size_price in sizes.items():
                item_name = f"{size.capitalize()} {food} with {topping}"
                total_price = food_price + topping_price + size_price
                order.drinks.append(item_name)
                order.total += total_price

    print(order.get_receipt())






from itertools import product

bases = ['water', 'pokecola', 'sbrite', 'Mr. salt', 'hill fog', 'leaf wine']
flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

drinks = [f"{base} with {flavor}" for base, flavor in product(bases, flavors)]

print(drinks)


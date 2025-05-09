import unittest
from Cinos import Order

class TestOrder(unittest.TestCase):
    def test_add_drink_and_total(self):
        order = Order()
        order.add_drink('water', 'lemon', 1.5)
        order.add_drink('pokecola', 'cherry', 3.25)
        self.assertEqual(order.get_total(), 4.75)
        self.assertIn('water with lemon', order.drinks)
        self.assertIn('pokecola with cherry', order.drinks)

    def test_get_receipt_format(self):
        order = Order()
        order.add_drink('sbrite', 'mint', 2.4)
        receipt = order.get_receipt()
        self.assertTrue(receipt.startswith("Order Receipt:"))
        self.assertIn("- sbrite with mint", receipt)
        self.assertIn("Total: $2.40", receipt)

    def test_empty_order(self):
        order = Order()
        self.assertEqual(order.get_total(), 0)
        receipt = order.get_receipt()
        self.assertIn("Total: $0.00", receipt)
        self.assertEqual(order.drinks, [])

    def test_large_order(self):
        order = Order()
        for i in range(100):
            order.add_drink('hill fog', 'blueberry', 3.8)
        self.assertEqual(order.get_total(), 380.0)
        receipt = order.get_receipt()
        self.assertEqual(receipt.count('- hill fog with blueberry'), 100)
        self.assertIn("Total: $380.00", receipt)

if __name__ == "__main__":
    unittest.main()


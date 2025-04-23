import pytest
from Cinos import Order

class TestOrder:
    def test_init(self):
        order = Order()
        assert order.drinks == []
        assert order.total == 0

class TestAddDrink:
    @pytest.mark.parametrize(
        "base, flavor, price, expected_drinks, expected_total",
        [
            pytest.param("water", "lemon", 1.50, ["water with lemon"], 1.50, id="single_drink"),
            pytest.param("soda", "lime", 2.00, ["soda with lime"], 2.00, id="different_drink"),
            pytest.param("water", "lemon", 0, ["water with lemon"], 0, id="zero_price"),  # Edge case: zero price
            pytest.param("", "", 1.50, [" with "], 1.50, id="empty_base_flavor"), # Edge case: empty base and flavor
        ],
    )
    def test_add_drink_happy_path(self, base, flavor, price, expected_drinks, expected_total):
        order = Order()
        order.add_drink(base, flavor, price)

        assert order.drinks == expected_drinks
        assert order.total == expected_total

    @pytest.mark.parametrize(
        "base, flavor, price, expected_error",
        [
            pytest.param("water", "lemon", "1.50", TypeError, id="price_is_string"),
            pytest.param(123, "lemon", 1.50, TypeError, id="base_is_int"),
            pytest.param("water", 456, 1.50, TypeError, id="flavor_is_int"),
            pytest.param("water", "lemon", -1.00, ValueError, id="negative_price"), # Error case: negative price
        ],
    )
    def test_add_drink_error_cases(self, base, flavor, price, expected_error):
        order = Order()

        with pytest.raises(expected_error):
            order.add_drink(base, flavor, price)


class TestGetTotal:
    @pytest.mark.parametrize(
        "total, expected_total",
        [
            pytest.param(0.0, 0.0, id="zero_total"),
            pytest.param(1.50, 1.50, id="positive_total"),
            pytest.param(10.75, 10.75, id="larger_positive_total"),
            pytest.param(0, 0, id="zero_integer_total"),  # Edge case: integer total
        ],
    )
    def test_get_total(self, total, expected_total):
        order = Order()
        order.total = total

        actual_total = order.get_total()

        assert actual_total == expected_total

class TestGetReceipt:
    @pytest.mark.parametrize(
        "drinks, total, expected_receipt",
        [
            pytest.param([], 0.0, "Order Receipt:\nTotal: $0.00", id="empty_order"),
            pytest.param(["water with lemon"], 1.50, "Order Receipt:\n- water with lemon\nTotal: $1.50", id="single_drink"),
            pytest.param(["water with lemon", "soda with lime"], 3.25, "Order Receipt:\n- water with lemon\n- soda with lime\nTotal: $3.25", id="multiple_drinks"),
            pytest.param(["water with lemon"], 0, "Order Receipt:\n- water with lemon\nTotal: $0.00", id="single_drink_zero_total"),  # Edge case: zero total
            pytest.param([], 10.5, "Order Receipt:\nTotal: $10.50", id="empty_order_non_zero_total"),  # Edge case: non-zero total with no drinks
        ],
    )
    def test_get_receipt_happy_path(self, drinks, total, expected_receipt):
        order = Order()
        order.drinks = drinks
        order.total = total

        actual_receipt = order.get_receipt()

        assert actual_receipt == expected_receipt
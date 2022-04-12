import pytest


@pytest.mark.usefixtures("setup_price_and_quantity_duck")
class TestPriceQuantityOfDucks:
    def test_quantity_of_duck(self, cart_page):
        quantity_on_page = cart_page.get_quantity_ducks_in_summary()

        assert quantity_on_page > 0, f"Quantity of duck must be more than 0"

    def test_price_of_duck(self, cart_page):
        total_price = cart_page.check_price_of_ducks()
        payment_due_price_of_ducks = cart_page.check_the_correctness_price_of_duck()

        assert total_price == payment_due_price_of_ducks, f"Expected {total_price}, but have {payment_due_price_of_ducks}"

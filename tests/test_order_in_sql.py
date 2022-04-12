import pytest


@pytest.mark.usefixtures("setup_price_and_quantity_duck")
class TestOrderId:
    def test_order_id(self, cart_page, sql_service):
        current_id = sql_service.get_id_of_order()
        cart_page.click_on_confirm_order_button()
        new_id = sql_service.get_id_of_order()
        final_id = current_id == new_id
        assert final_id + 1, f"Orders were not found"

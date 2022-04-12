from pages.base_page import BasePage


class CartPage(BasePage):
    CHECK_QUANTITY_OF_DUCKS_LOCATOR = "//td[contains(@style,'text-align: center')]"
    SUM_COSTS_OF_DUCK_LOCATOR = "//td[@class='sum']"
    CONFIRM_ORDER_LOCATOR = "//button[@name='confirm_order']"
    PAYMENT_DUE_PRICE_OF_DUCKS = "//strong[contains(text(),'$')]"

    def scroll_down_on_page(self):
        self.scroll_down()

    def click_on_confirm_order_button(self):
        self.click(self.CONFIRM_ORDER_LOCATOR)

    def get_quantity_ducks_in_summary(self):
        return int(self.get_text(self.CHECK_QUANTITY_OF_DUCKS_LOCATOR))

    def check_price_of_ducks(self):
        return self.get_text(self.SUM_COSTS_OF_DUCK_LOCATOR)

    def check_the_correctness_price_of_duck(self):
        return self.get_text(self.PAYMENT_DUE_PRICE_OF_DUCKS)


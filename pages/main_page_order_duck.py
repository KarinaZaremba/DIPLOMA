from pages.base_page import BasePage


class OrderPage(BasePage):
    URL = "http://localhost/litecart/en/"

    EMAIL_LOCATOR = "//input[@name='email']"
    PASS_LOCATOR = "//input[@name='password']"
    LOGIN_BUTTON_LOCATOR = "//button[@name='login']"

    DUCK_LOCATOR = "//div[@class='image-wrapper']"
    QUANTITY_LOCATOR = "//input[@name='quantity']"
    ADD_TO_CART_LOCATOR = "//button[@name='add_cart_product']"
    CHECK_OUT_LOCATOR = "//a[contains(text(),'Checkout')]"
    QUANTITY_CHECKOUT_CART_LOCATOR = "//span[text()='{}']"

    def navigate(self):
        self.open_url(self.URL)
        self.maximize_window()

    def enter_email(self, email):
        self.enter_text(self.EMAIL_LOCATOR, email)

    def enter_password(self, password):
        self.enter_text(self.PASS_LOCATOR, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON_LOCATOR)

    def login_correct_data(self, email, password):
        self.enter_text(self.EMAIL_LOCATOR, email)
        self.enter_text(self.PASS_LOCATOR, password)
        self.click(self.LOGIN_BUTTON_LOCATOR)

    def choose_duck(self):
        self.click(self.DUCK_LOCATOR)

    def change_quantity(self, text):
        self.click(self.QUANTITY_LOCATOR)
        self.delete_element(self.QUANTITY_LOCATOR)
        self.enter_text(self.QUANTITY_LOCATOR, text)
        self.click(self.ADD_TO_CART_LOCATOR)
        self.wait_for_element_present(self.QUANTITY_CHECKOUT_CART_LOCATOR.format("3"))

    def click_on_checkout_button(self):
        self.click(self.CHECK_OUT_LOCATOR)

    def get_quantity_duck(self):
        self.navigate()
        self.login_correct_data("Karina@tut.by", "11111")
        self.choose_duck()
        self.change_quantity("3")
        self.click_on_checkout_button()

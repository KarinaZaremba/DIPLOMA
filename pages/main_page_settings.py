from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "http://localhost/litecart/en/"

    REGIONAL_SETTING = "//a[@class='fancybox-region']"
    SAVE_LOCATOR = "//button[@name= 'save']"

    COUNTRY_CODE_LOCATOR = "//select[@name = 'country_code']"
    COUNTRY_LOCATOR = "//option[text()='{}']"

    CURRENCY_BUTTON_LOCATOR = "//select[@name='currency_code']"
    CURRENCY_LOCATOR = "//option[text() = 'Euros']"

    TITLE_TEXT_MAIN_PAGE_LOCATOR = "//div[@title='{}']"

    def navigate(self):
        self.open_url(self.URL)
        self.maximize_window()

    def click_on_change_button(self):
        self.click(self.REGIONAL_SETTING)

    def click_save_button(self):
        self.click(self.SAVE_LOCATOR)

    def change_country(self, country):
        self.click(self.COUNTRY_CODE_LOCATOR)
        self.click(self.COUNTRY_LOCATOR.format(country))

    def change_currency(self, currency):
        self.click(self.CURRENCY_BUTTON_LOCATOR)
        self.click(self.CURRENCY_LOCATOR.format(currency))

    def change_country_and_currency(self):
        self.navigate()
        self.click_on_change_button()
        self.change_country("Ukraine")
        self.change_currency("Euros")
        self.click_save_button()

    def get_title_country(self, country_title):
        return self.get_text(self.TITLE_TEXT_MAIN_PAGE_LOCATOR.format(country_title))

    def get_title_currency(self, currency_title):
        return self.get_text(self.TITLE_TEXT_MAIN_PAGE_LOCATOR.format(currency_title))


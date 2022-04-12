import pytest


@pytest.mark.usefixtures("setup_test_regional_settings")
class TestValuesCountryCurrency:
    def test_change_country(self, main_page):
        currency_value = "EUR"
        new_value = main_page.get_title_currency("Euros")
        assert currency_value == new_value, f"We're expecting {currency_value} , but was {new_value}"

    def test_change_currency(self, main_page):
        country_value = "Ukraine"
        new_value = main_page.get_title_country("Ukraine")
        assert country_value == new_value, f"We're expecting {country_value} , but was {new_value}"


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page_settings import MainPage
from pages.main_page_order_duck import OrderPage
from pages.cart_page import CartPage
from mysql.connector import connect
from pages.sql_service_order_ducks import SqlService


@pytest.fixture()
def setup_test_regional_settings(chromedriver, main_page):
    main_page.change_country_and_currency()

    yield
    chromedriver.quit()


@pytest.fixture()
def setup_price_and_quantity_duck(chromedriver, main_page_order_duck, cart_page):
    main_page_order_duck.get_quantity_duck()
    cart_page.scroll_down_on_page()

    yield
    chromedriver.quit()


@pytest.fixture()
def connection_to_data_base():
    connection = connect(host="localhost",
                         user="root",
                         password="",
                         database='litecart'
                         )
    yield connection
    connection.close()


@pytest.fixture()
def sql_service(connection_to_data_base):
    return SqlService(connection_to_data_base)


@pytest.fixture()
def chromedriver():
    return webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture()
def main_page(chromedriver):
    return MainPage(chromedriver)


@pytest.fixture()
def main_page_order_duck(chromedriver):
    return OrderPage(chromedriver)


@pytest.fixture()
def cart_page(chromedriver):
    return CartPage(chromedriver)

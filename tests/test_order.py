import allure
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.order_page import OrderPage


class TestOrder:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.maximize_window()

    @allure.title('Проверка оформления самоката')
    @pytest.mark.parametrize(
        'name,surname,addres,phone',
        [
            ['Имя', 'Фамилия', 'Адрес', '89608447444'],
            ['Ольга', 'Иванова', 'Волгоград', '89608447443']
        ]
    )

    def test_order(self, name, surname, addres, phone):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        order_pages = OrderPage(self.driver)
        order_pages.click_order_tab()
        order_pages.wait_whose_order()
        order_pages.fill_name(name)
        order_pages.fill_surname(surname)
        order_pages.fill_addres(addres)
        order_pages.click_metro_tab()
        order_pages.wait_stations()
        order_pages.click_select_tab()
        order_pages.fill_phone(phone)
        order_pages.click_further_tab()
        order_pages.wait_back_tab()
        order_pages.click_time_tab()
        order_pages.click_select_day()
        order_pages.click_rental_period()
        order_pages.wait_list()
        order_pages.click_day_selection()
        order_pages.click_select_color()
        order_pages.wait_checkbox()
        order_pages.fill_comment()
        order_pages.click_click_order()
        order_pages.wait_clarification()
        order_pages.click_yes_tab()
        order_pages.wait_successfully_complited()
        status = order_pages.check_status()

        assert status == 'Посмотреть статус'
        self.driver.quit()
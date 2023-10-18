import allure
import pytest

from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка оформления самоката')
    @pytest.mark.parametrize(
        'name,surname,address,phone, comment',
        [
            ['Имя', 'Фамилия', 'Адрес', '89608447444', 'без комментариев'],
            ['Ольга', 'Иванова', 'Волгоград', '89608447443', 'нет комментов']
        ]
    )

    def test_order(self, driver, name, surname, address, phone, comment):
        order_pages = OrderPage(driver)
        order_pages.get_url("https://qa-scooter.praktikum-services.ru/")
        order_pages.click_order_tab()
        order_pages.filling_fields(name, surname, address, phone, comment)
        order_pages.click_yes_tab()
        order_pages.wait_successfully_complited()
        status = order_pages.check_status()

        assert status == 'Посмотреть статус'
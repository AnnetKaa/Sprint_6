import allure
from pages.jump_page import JumpPage

class TestJump:

    @allure.title('Проверка перехода на страницу Дзен')
    def test_jump_to_yandex(self, driver):
        jump_pages = JumpPage(driver)
        jump_pages.get_url("https://qa-scooter.praktikum-services.ru/order")
        jump_pages.click_yandex_tab()
        jump_pages.wait_switch_to_window(1)
        jump_pages.wait_dzen_site()
        actual_url = jump_pages.find_actual_url()
        assert actual_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверка перехода на главную страницу')
    def test_jump_to_main_page(self, driver):
        jump_pages = JumpPage(driver)
        jump_pages.get_url("https://qa-scooter.praktikum-services.ru/order")
        jump_pages.click_main_tab()
        jump_pages.wait_main_site()
        actual_url = jump_pages.find_actual_url()
        assert actual_url == "https://qa-scooter.praktikum-services.ru/"
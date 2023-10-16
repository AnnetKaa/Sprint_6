import allure
from selenium import webdriver
from pages.jump_page import JumpPage

class TestJump:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка перехода на страницу Дзен')
    def test_jump_to_yandex(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        jump_pages = JumpPage(self.driver)
        jump_pages.click_yandex_tab()
        jump_pages.wait_switch_to_window()
        jump_pages.wait_dzen_site()
        actual_url = jump_pages.find_actual_url()
        assert actual_url == 'https://dzen.ru/?yredirect=true'
        self.driver.close()
        self.driver.quit()

    @allure.title('Проверка перехода на главную страницу')
    def test_jump_to_main_page(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        jump_pages = JumpPage(self.driver)
        jump_pages.click_main_tab()
        jump_pages.wait_main_site()
        actual_url = jump_pages.find_actual_url()
        assert actual_url == "https://qa-scooter.praktikum-services.ru/"
        self.driver.quit()
import allure
from pages.base_page import BasePage
from locators import locators_jump


class JumpPage(BasePage):
    locators = locators_jump.LocatorsforJump()

    @allure.step('Переходим по табу яндекс')
    def click_yandex_tab(self):
        self.find_element(self.locators.YANDEX).click()

    @allure.step('Нажимаем логотип самоката')
    def click_main_tab(self):
        self.find_element(self.locators.MAIN).click()

    @allure.step('Ожидаем открытие страницы')
    def wait_dzen_site(self):
        self.wait_presence_of_element_located(self.locators.DZEN)

    @allure.step('Ожидаем открытия главной страницы')
    def wait_home_site(self):
        self.wait_presence_of_element_located(self.locators.HOME)

    @allure.step('Открытие новой вкладки')
    def wait_switch_to_window(self, index):
        self.switch_to_window(index)
        self.wait_presence_of_element_located(self.locators.DZEN)
        return self.find_actual_url()

    @allure.step('Ожидаем открытия главной страницы')
    def wait_main_site(self):
        self.wait_presence_of_element_located(self.locators.IMG)



import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import locators_jump


class JumpPage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим по табу яндекс')
    def click_yandex_tab(self):
        self.driver.find_element(*locators_jump.LocatorsforJump.YANDEX).click()

    @allure.step('Ожидаем открытие страницы')
    def wait_dzen_site(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locators_jump.LocatorsforJump.DZEN))

    @allure.step('Нажимаем логотип самоката')
    def click_main_tab(self):
        self.driver.find_element(*locators_jump.LocatorsforJump.MAIN).click()

    @allure.step('Ожидаем открытия главной страницы')
    def wait_home_site(self):
        WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(locators_jump.LocatorsforJump.HOME))

    @allure.step('Открытие новой вкладки')
    def wait_switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверка актуального URL')
    def find_actual_url(self):
        return self.driver.current_url

    @allure.step('Ожидаем открытия главной страницы')
    def wait_main_site(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locators_jump.LocatorsforJump.IMG))

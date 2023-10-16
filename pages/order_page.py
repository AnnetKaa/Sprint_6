import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators_order

class OrderPage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку заказа')
    def click_order_tab(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.ORDER_TAB).click()

    @allure.step('Ждем окно для заполнения')
    def wait_whose_order(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(
            (locators_order.LocatorsforOrder.WHOSE_ORDER)))

    @allure.step('Заполнить имя')
    def fill_name(self, name):
        self.driver.find_element(*locators_order.LocatorsforOrder.NAME).send_keys(name)

    @allure.step('Заполнить фамилию')
    def fill_surname(self, surname):
        self.driver.find_element(*locators_order.LocatorsforOrder.SURNAME).send_keys(surname)

    @allure.step('Заполнить адрес')
    def fill_addres(self, addres):
        self.driver.find_element(*locators_order.LocatorsforOrder.ADDRES).send_keys(addres)

    @allure.step('Нажать на станцию метро')
    def click_metro_tab(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.METRO).click()

    @allure.step('Ожидаем открытия списка')
    def wait_stations(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((locators_order.LocatorsforOrder.STATIONS)))

    @allure.step('Выбрать станцию метро')
    def click_select_tab(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.SELECT).click()

    @allure.step('Заполнить телефон')
    def fill_phone(self, phone):
        self.driver.find_element(*locators_order.LocatorsforOrder.PHONE).send_keys(phone)

    @allure.step('Нажать Далее')
    def click_further_tab(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.FURTHER_TAB).click()

    @allure.step('Ожидание кнопки Назад')
    def wait_back_tab(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_order.LocatorsforOrder.BACK_TAB)))

    @allure.step('Нажать кнопку календаря')
    def click_time_tab(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.TIME).click()

    @allure.step('Выбрать день')
    def click_select_day(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.DAY).click()

    @allure.step('Клик периода')
    def click_rental_period(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.RENTAL_PERIOD).click()

    @allure.step('Ожидаем список')
    def wait_list(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_order.LocatorsforOrder.LIST)))

    @allure.step('Выбрать день')
    def click_day_selection(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.DAY_SELECTION).click()

    @allure.step('Выбрать цвет')
    def click_select_color(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.COLOR).click()

    @allure.step('ожидание чекбокса')
    def wait_checkbox(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_order.LocatorsforOrder.CHECKBOX)))

    @allure.step('Заполнить коммент')
    def fill_comment(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.COMMENT).send_keys('Без комментариев')

    @allure.step('Нажать заказать')
    def click_click_order(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.CLICK_ORGER).click()

    @allure.step('Ожидаение уточнения')
    def wait_clarification(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(
            (locators_order.LocatorsforOrder.CLARIFICATION)))

    @allure.step('Нажать ДА')
    def click_yes_tab(self):
        self.driver.find_element(*locators_order.LocatorsforOrder.YES_TAB).click()

    @allure.step('Ожидание успешного заполнения')
    def wait_successfully_complited(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(
            (locators_order.LocatorsforOrder.SUCCESSFULLY_COMPLITED)))

    @allure.step('Проверить статус')
    def check_status(self):
        return self.driver.find_element(*locators_order.LocatorsforOrder.STATUS).text



    


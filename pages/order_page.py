import allure
from locators import locators_order
from pages.base_page import BasePage

class OrderPage(BasePage):
    locators = locators_order.LocatorsforOrder()

    @allure.step('Нажимаем кнопку заказа')
    def click_order_tab(self):
        self.find_element(self.locators.ORDER_TAB).click()
        self.wait_element_to_be_clickable(self.locators.WHOSE_ORDER)

    def filling_fields(self, name, surname, address, phone, comment):
        self.find_element(self.locators.NAME).send_keys(name)
        self.find_element(self.locators.SURNAME).send_keys(surname)
        self.find_element(self.locators.ADDRES).send_keys(address)
        self.find_element(self.locators.METRO).click()
        self.wait_element_to_be_clickable(self.locators.STATIONS)
        self.find_element(self.locators.SELECT).click()
        self.find_element(self.locators.PHONE).send_keys(phone)
        self.find_element(self.locators.FURTHER_TAB).click()
        self.wait_element_to_be_clickable(self.locators.BACK_TAB)
        self.find_element(self.locators.TIME).click()
        self.find_element(self.locators.DAY).click()
        self.find_element(self.locators.RENTAL_PERIOD).click()
        self.wait_element_to_be_clickable(self.locators.LIST)
        self.find_element(self.locators.DAY_SELECTION).click()
        self.find_element(self.locators.COLOR).click()
        self.wait_element_to_be_clickable(self.locators.CHECKBOX)
        self.find_element(self.locators.COMMENT).send_keys(comment)
        self.find_element(self.locators.CLICK_ORGER).click()
        self.wait_element_to_be_clickable(self.locators.CLARIFICATION)

    @allure.step('Нажать ДА')
    def click_yes_tab(self):
        self.find_element(self.locators.YES_TAB).click()

    @allure.step('Ожидание успешного заполнения')
    def wait_successfully_complited(self):
        self.wait_element_to_be_clickable(self.locators.SUCCESSFULLY_COMPLITED)

    @allure.step('Проверить статус')
    def check_status(self):
        return self.find_element(self.locators.STATUS).text


    


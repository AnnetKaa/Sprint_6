import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators_question

class QuestionsPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл страницы')
    def scroll(self):
        element = self.driver.find_element(*locators_question.LocatorsforQuestion.IMPORTANT_QUESTIONS)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажать вопрос цены')
    def click_price_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.PRICE_QUESTION).click()

    @allure.step('Дождаться ответа по цене')
    def wait_price_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.PRICE_ANSWER)))

    @allure.step('Сверить ответ по цене')
    def find_price_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.PRICE_ANSWER).text

    @allure.step('Нажать вопрос количества')
    def click_quantity_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.QUANTITY_QUESTION).click()

    @allure.step('Ожидание ответа по количеству')
    def wait_quantity_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.QUANTITY_ANSWER)))

    @allure.step('Сверить ответ по количеству')
    def find_quantity_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.QUANTITY_ANSWER).text

    @allure.step('Нажать вопрос времени')
    def click_time_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.TIME_QUESTION).click()

    @allure.step('Ожидание ответа по времени')
    def wait_time_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.TIME_ANSWER)))

    @allure.step('Сверить ответ по времени')
    def find_time_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.TIME_ANSWER).text

    @allure.step('Нажать вопрос по заказу сегодня')
    def click_order_today_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.ORDER_TODAY_QUESTION).click()

    @allure.step('Ожидание ответа по заказу сегодня')
    def wait_order_today_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.ORDER_TODAY_ANSWER)))

    @allure.step('Сверить ответ по заказу сегодня')
    def find_order_today_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.ORDER_TODAY_ANSWER).text

    @allure.step('Нажать вопрос дедлайна')
    def click_deadline_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.DEADLINE_QUESTION).click()

    @allure.step('Ожидание ответа по дедлайну')
    def wait_deadline_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.DEADLINE_ANSWER)))

    @allure.step('Сверить ответ по дедлайну')
    def find_deadline_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.DEADLINE_ANSWER).text

    @allure.step('Нажать вопрос по зарядке')
    def click_charger_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.CHARGER_QUESTION).click()

    @allure.step('Ожидание ответа по зарядке')
    def wait_charger_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.CHARGER_ANSWER)))

    @allure.step('Сверка ответа по зарядке')
    def find_charger_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.CHARGER_ANSWER).text

    @allure.step('Нажать вопрос по отмене')
    def click_cancel_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.CANCEL_QUESTION).click()

    @allure.step('Ожидание ответа по отмене')
    def wait_cancel_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.CANCEL_ANSWER)))

    @allure.step('Сверить ответ по отмене')
    def find_cancel_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.CANCEL_ANSWER).text

    @allure.step('Нажать вопрос по территории')
    def click_territory_question(self):
        self.driver.find_element(*locators_question.LocatorsforQuestion.TERRITORY_QUESTION).click()

    @allure.step('Ожидание ответа по территории')
    def wait_territory_answer(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.element_to_be_clickable((locators_question.LocatorsforQuestion.TERRITORY_ANSWER)))

    @allure.step('Сверить ответ по территории')
    def find_territory_answer(self):
        return self.driver.find_element(*locators_question.LocatorsforQuestion.TERRITORY_ANSWER).text


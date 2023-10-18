import allure

from locators import locators_question
from pages.base_page import BasePage

class QuestionsPage(BasePage):
    locators = locators_question.LocatorsforQuestion()

    @allure.step('Скролл страницы')
    def scroll_to_questions(self):
        element = self.find_element(self.locators.IMPORTANT_QUESTIONS)
        self.scroll(element)

    @allure.step('Нажимаем на вопрос')
    def click_question(self, question):
        self.find_element(question).click()

    @allure.step('Находим ответ')
    def look_answer(self, answer):
        actual_answer = self.find_element(answer).text
        return actual_answer





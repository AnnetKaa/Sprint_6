import allure
import pytest

# import locators
from locators import locators_question
from pages.question_page import QuestionsPage

class TestQuestions:

    @allure.title('Проверка работы блока вопросов и ответов')
    @pytest.mark.parametrize(
        "question, answer, expected_answer",
        [
            [locators_question.LocatorsforQuestion.QUESTION_1,
             locators_question.LocatorsforQuestion.ANSWER_1,
             'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
            [locators_question.LocatorsforQuestion.QUESTION_2,
             locators_question.LocatorsforQuestion.ANSWER_2,
             'Пока что у нас так: один заказ — один самокат. '
             'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
            [locators_question.LocatorsforQuestion.QUESTION_3,
             locators_question.LocatorsforQuestion.ANSWER_3,
             'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
             'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
             'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
            [locators_question.LocatorsforQuestion.QUESTION_4,
             locators_question.LocatorsforQuestion.ANSWER_4,
             'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
            [locators_question.LocatorsforQuestion.QUESTION_5,
             locators_question.LocatorsforQuestion.ANSWER_5,
             'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
            [locators_question.LocatorsforQuestion.QUESTION_6,
             locators_question.LocatorsforQuestion.ANSWER_6,
             'Самокат приезжает к вам с полной зарядкой. '
             'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
            [locators_question.LocatorsforQuestion.QUESTION_7,
             locators_question.LocatorsforQuestion.ANSWER_7,
             'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
            [locators_question.LocatorsforQuestion.QUESTION_8,
             locators_question.LocatorsforQuestion.ANSWER_8,
             'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ]
    )
    def test_accordian_content(self, driver, question, answer, expected_answer):
        question_pages = QuestionsPage(driver)
        question_pages.get_url("https://qa-scooter.praktikum-services.ru/")
        question_pages.scroll_to_questions()
        question_pages.click_question(question)
        actual_answer = question_pages.look_answer(answer)
        assert actual_answer == expected_answer



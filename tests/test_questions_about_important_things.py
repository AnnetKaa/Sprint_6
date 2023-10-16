import allure
from selenium import webdriver
from pages.question_page import QuestionsPage

class TestQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка визуацизации вопроса по цене')
    def test_prise(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_price_question()
        question_pages.wait_price_answer()
        price_answer = question_pages.find_price_answer()
        assert price_answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        self.driver.quit()

    @allure.title('Проверка визуацизации вопроса по количеству')
    def test_quantity(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_quantity_question()
        question_pages.wait_quantity_answer()
        quantity_answer = question_pages.find_quantity_answer()
        assert quantity_answer == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        self.driver.quit()

    @allure.title('Проверка визуацизации вопроса по времени')
    def test_time(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_time_question()
        question_pages.wait_time_answer()
        time_answer = question_pages.find_time_answer()
        assert time_answer == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        self.driver.quit()

    @allure.title('Проверка визуацизации вопроса по заказу на сегодня')
    def test_order_today(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_order_today_question()
        question_pages.wait_order_today_answer()
        order_today = question_pages.find_order_today_answer()
        assert order_today == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        self.driver.quit()

    @allure.title('Проверка визуацизации вопроса по дедлайну')
    def test_deadline(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_deadline_question()
        question_pages.wait_deadline_answer()
        deadline_answer = question_pages.find_deadline_answer()
        assert deadline_answer == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        self.driver.quit()

    @allure.title('Проверка визуацизации вопроса по зарядке')
    def test_charger(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_charger_question()
        question_pages.wait_charger_answer()
        charger_answer = question_pages.find_charger_answer()
        assert charger_answer == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        self.driver.quit()

    @allure.title('Проверка визуацизации вопроса по отмене заказа')
    def test_cancel(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_cancel_question()
        question_pages.wait_cancel_answer()
        cancel_answer = question_pages.find_cancel_answer()
        assert cancel_answer == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        self.driver.quit()

    @allure.title('Проверка визуацизации вопроса по территории')
    def test_territory(self):
        self.setup_class()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_pages = QuestionsPage(self.driver)
        question_pages.scroll()
        question_pages.click_territory_question()
        question_pages.wait_territory_answer()
        territory_answer = question_pages.find_territory_answer()
        assert territory_answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        self.driver.quit()
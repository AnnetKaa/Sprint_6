from selenium.webdriver.common.by import By

class LocatorsforJump:
    YANDEX = (By.XPATH, ".//img[@alt = 'Yandex']")
    DZEN = (By.XPATH, ".//a[@title = 'ОК']")
    MAIN = (By.XPATH, ".//img[@alt = 'Scooter']")
    HOME = (By.XPATH, ".//a[contains(text() ='на пару дней')]")
    IMG = (By.XPATH, './/img[@alt="Scooter blueprint"]')
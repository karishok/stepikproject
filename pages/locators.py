from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN = "login"

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    STRONG_SELECTOR = (By.TAG_NAME, "strong")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
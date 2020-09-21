from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN = "login"
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    STRONG_SELECTOR = (By.TAG_NAME, "strong")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_SUMMARY = (By.CLASS_NAME, "basket_summary")




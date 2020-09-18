from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket.click()

    def is_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_elements(*ProductPageLocators.STRONG_SELECTOR)[3].text, "Product not in basket"

    def is_price_is_true(self):
        x = self.browser.find_elements(*ProductPageLocators.PRODUCT_PRICE)[1].text
        y = self.browser.find_elements(*ProductPageLocators.STRONG_SELECTOR)[5].text
        assert x == y, f"Price is wrong {(x,y)}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def diapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
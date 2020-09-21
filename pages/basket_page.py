from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "There are products in basket"

    def show_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"

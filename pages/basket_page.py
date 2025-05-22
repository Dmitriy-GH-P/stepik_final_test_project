from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_text(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert "empty" in basket_text, 'Your basket is not empty'

    def should_not_be_any_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), \
            "Your basket is not empty, but should be"
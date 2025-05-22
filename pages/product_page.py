from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def book_is_added(self):
        your_item_name = self.browser.find_element(*ProductPageLocators.ITEM_THAT_YOU_WANNA_ADD).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert your_item_name in success_message, "Your item not added"
        print(success_message)

    def basket_value(self):
        basket_value = self.browser.find_element(*ProductPageLocators.YOUR_BASKET_VALUE).text
        your_item_value = self.browser.find_element(*ProductPageLocators.YOUR_ITEM_VALUE).text
        assert  basket_value == your_item_value
        print(f'Your basket value is {basket_value}')

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):

    def should_be_promo(self):
        current_url = self.browser.current_url
        assert "?promo=newYear" in current_url, "Not a promo"

    def add_to_card(self):
        add_to_card_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD)
        add_to_card_button.click()


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
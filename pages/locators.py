from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CARD = (By.CSS_SELECTOR, "button.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_THAT_YOU_WANNA_ADD = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in")
    ITEM_THAT_WAS_ADDED = (By.CSS_SELECTOR, "div.alertinner strong")
    YOUR_ITEM_VALUE = (By.CSS_SELECTOR, "p.price_color")
    YOUR_BASKET_VALUE = (By.CSS_SELECTOR, "div.alertinner p strong")
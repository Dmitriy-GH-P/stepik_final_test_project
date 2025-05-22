from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_CARD = (By.CSS_SELECTOR, "button.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_THAT_YOU_WANNA_ADD = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in")
    ITEM_THAT_WAS_ADDED = (By.CSS_SELECTOR, "div.alertinner strong")
    YOUR_ITEM_VALUE = (By.CSS_SELECTOR, "p.price_color")
    YOUR_BASKET_VALUE = (By.CSS_SELECTOR, "div.alertinner p strong")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    BASKET_TEXT = (By.CSS_SELECTOR, "div#content_inner p")
    ITEMS_TO_BUY = (By.CSS_SELECTOR, "form#basket_formset.basket_summary")
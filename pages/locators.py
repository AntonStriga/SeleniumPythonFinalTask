from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRMATION_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductsPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MAIN_PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    MAIN_PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/*[@class='price_color']")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    BASKET_TOTAL_SUM = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")

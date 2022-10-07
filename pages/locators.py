from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductsPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MAIN_PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    MAIN_PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/*[@class='price_color']")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    BASKET_TOTAL_SUM = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

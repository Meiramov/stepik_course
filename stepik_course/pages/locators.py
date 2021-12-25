from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.XPATH, ("//button[[@type, 'submit'] and [@value, 'Log In']]"))

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ItemToBasketLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.TAG_NAME, 'h1')
    BOOK_PRICE = (By.XPATH, '//*[@class = "col-sm-6 product_main"]//*[@class = "price_color"]')
    NOTIFIER_BOOK_NAME = (By.XPATH, "//*[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")
    NOTIFIER_BOOK_PRICE = (By.XPATH, "//*[@class='row']//*[@class='basket-mini pull-right hidden-xs']")

from pages.base_page import BasePage
from pages.locators import ItemToBasketLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage


class ItemPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ItemToBasketLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_alert(self):
        self.solve_quiz_and_get_code()

    def assert_item_in_basket(self):
        assert self.is_element_present(*ItemToBasketLocators.ADD_TO_BASKET), "Item not added to basket"

    # Проверка названия книги разбита на три метода
    def book_name(self):
        book_name = self.browser.find_element(*ItemToBasketLocators.BOOK_NAME)
        book_name = book_name.text
        return book_name

    def notifier_book(self):
        notifier_book = self.browser.find_element(*ItemToBasketLocators.NOTIFIER_BOOK_NAME)
        notifier_book = notifier_book.text
        return notifier_book
        
    def assert_book_name(self):
        assert self.book_name() in self.notifier_book(), "Not correct book were added to basket"

    # Проверка цены на книгу написана в одном методе, не уверен как читабельнее и лучше по архитектуре :)
    def assert_item_price(self):
        book_price = self.browser.find_element(*ItemToBasketLocators.BOOK_PRICE)
        book_price = book_price.text
        notifier_price = self.browser.find_element(*ItemToBasketLocators.NOTIFIER_BOOK_PRICE)
        notifier_price = notifier_price.text

        assert book_price in notifier_price, "Price is not correct"

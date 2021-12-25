from pages.product_page import ItemPage
import time



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ItemPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.assert_item_in_basket()
    page.add_item_to_basket()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_alert()
    page.assert_book_name()
    page.assert_item_price()
    # time.sleep(600)

# from selenium import webdriver
# import pytest
# from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/"


# # @pytest.fixture(autouse=True)
# # def prepare_data():
# #     print()
# #     print("Preparing data")

# class TestMainPage1():
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")

#     @pytest.mark.regress
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

#     @pytest.mark.xfail(reason="Bug fixing in progress")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, 'button.favorite')

#     @pytest.mark.test_param
#     @pytest.mark.parametrize('language', ['ru', 'en-gb'])
#     def test_guest_should_see_login_link(self, browser, language):
#         link = f"http://selenium1py.pythonanywhere.com/{language}/"
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")

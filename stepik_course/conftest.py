from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose any language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    # link = None
    # if browser_language == "es":
    #     print('Test ES')
    #     link = f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/"

    # elif browser_language == "ru":
    #     print('Test ES')
    #     link = f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/"

    # elif browser_language == "fr":
    #     print('Test ES')
    #     link = f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/"
    link = f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    # options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name=="chrome":
        print("\n Start chrome browser")
        browser = webdriver.Chrome()
        # browser = webdriver.Chrome(options=options)
    elif browser_name=="firefox":
        print("\n Start firefox browser")
        browser = webdriver.Firefox()
    else:
        print("--browser_name should be chrome or firefox")
    # print("\nstart browser for test..")
    # browser = webdriver.Chrome()
    #browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture(scope="function")
# def language(request, browser):
#     browser_language = request.config.getoption("language")
#     link = None
#     if browser_language == "es":
#         print('Test ES')
#         link = f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/"
#     browser.get(link)
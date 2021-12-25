from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkbutton_add(browser):
    time.sleep(5)
    basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    name_of_book = browser.find_element(By.TAG_NAME, 'h1')
    name_of_book = name_of_book.text

    assert name_of_book == "Coders at Work", "Не та книга"

    basket_button.click()

    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "messages"))
    )

    browser.find_element(By.XPATH, "//*[@id='messages']//*[contains(text(), '"+name_of_book+"')]")

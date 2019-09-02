# Run me with: pytest -v -s --tb=line
import time
from selenium import webdriver

URL = 'http://selenium1py.pythonanywhere.com/catalogue/kingpin_186/'

def test_guest_see_add_to_basket_button(browser):
    browser.get(URL)
    btn = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert btn.is_enabled()
    print('\n[DEBUG] visited URL: {}'.format(browser.current_url))
    print('[DEBUG] found button with text: {}'.format(btn.text))

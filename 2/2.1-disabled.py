from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/math.html')

button = browser.find_element_by_css_selector('button.btn-default')
button_disabled = button.get_attribute('disabled')
print('Button disabled value:', button_disabled)

time.sleep(15)

button_disabled = button.get_attribute('disabled')
print('Button disabled value:', button_disabled)

assert button_disabled == 'true'
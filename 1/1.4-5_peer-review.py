from selenium import webdriver
import time

URL = 'http://suninjuly.github.io/registration1.html'
#URL = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()
browser.get(URL)

first_name_input = browser.find_element_by_css_selector('div.first_block input.first')
first_name_input.send_keys('Stanley')

last_name_input = browser.find_element_by_css_selector('div.first_block input.second')
last_name_input.send_keys('Nobody')

email_input = browser.find_element_by_css_selector('div.first_block input.third')
email_input.send_keys('a@b.c')

time.sleep(1)

submit_button = browser.find_element_by_tag_name('button')
submit_button.click()

result = browser.find_element_by_tag_name('h1')
assert result.text == "Поздравляем! Вы успешно зарегистировались!"

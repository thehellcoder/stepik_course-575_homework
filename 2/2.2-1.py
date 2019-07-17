from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

num1 = browser.find_element_by_id('num1')
num2 = browser.find_element_by_id('num2')
sum = int(num1.text) + int(num2.text)
print(num1.text, '+', num2.text, '=', sum)

select = Select(browser.find_element_by_tag_name('select'))
select.select_by_value(str(sum))

submit_button = browser.find_element_by_css_selector('button.btn-default')
submit_button.click()

time.sleep(15)

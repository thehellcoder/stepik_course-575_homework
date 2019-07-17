from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

chest_elem = browser.find_element_by_id('treasure')
x = chest_elem.get_attribute('valuex')
result = calc(x)
print('x=', x, ' result=', result)

answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(result)

robot_checkbox = browser.find_element_by_id('robotCheckbox')
robot_checkbox.click()

robot_radio = browser.find_element_by_id('robotsRule')
robot_radio.click()

submit_button = browser.find_element_by_css_selector('button.btn-default')
submit_button.click()

time.sleep(30)
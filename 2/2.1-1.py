from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

URL = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(URL)

x = browser.find_element_by_id('input_value')
result = calc(x.text)
print('x=', x.text, 'result=', result)

answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(result)

chkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
chkbox.click()

radio = browser.find_element_by_css_selector('[for="robotsRule"]')
radio.click()

submit_button = browser.find_element_by_css_selector('button.btn-default')
submit_button.click()

time.sleep(10)

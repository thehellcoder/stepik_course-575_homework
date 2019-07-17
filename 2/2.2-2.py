from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/execute_script.html')

x = browser.find_element_by_id('input_value')
result = calc(x.text)
print('x=', x.text, 'result=', result)

answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(result)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radio = browser.find_element_by_id('robotsRule')
browser.execute_script('arguments[0].scrollIntoView(true);', radio)
radio.click()

button = browser.find_element_by_css_selector('button.btn-default')
button.click()

time.sleep(10)
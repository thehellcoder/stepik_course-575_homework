from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/alert_accept.html')
button = browser.find_element_by_tag_name('button')
button.click()
confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id('input_value')
result = calc(x.text)
print('x=', x.text, 'result=', result)
answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(result)

submit_button = browser.find_element_by_css_selector('button.btn-primary')
submit_button.click()
alert = browser.switch_to.alert
print(alert.text)

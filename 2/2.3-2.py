from selenium import webdriver
import math

def calc(x):
    x = x.text
    result = str(math.log(abs(12*math.sin(int(x)))))
    print('x=', x, 'result=', result)
    return result

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/redirect_accept.html')
button = browser.find_element_by_css_selector('button.trollface')
button.click()

browser.switch_to.window(browser.window_handles[1])
x = browser.find_element_by_id('input_value')
result = calc(x)
answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(result)
button_submit = browser.find_element_by_css_selector('button.btn-primary')
button_submit.click()
alert = browser.switch_to.alert
print(alert.text)

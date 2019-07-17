from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    x = x.text
    result = math.log(abs(12*math.sin(int(x))))
    print('x=', x, 'result=', result)
    return str(result)

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000'))
button_book = browser.find_element_by_id('book')
button_book.click()

x = browser.find_element_by_id('input_value')
result = calc(x)
answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(result)
button_solve = browser.find_element_by_id('solve')
button_solve.click()

alert = browser.switch_to.alert
print(alert.text)

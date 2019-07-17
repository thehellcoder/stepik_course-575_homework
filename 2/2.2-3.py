from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

fname = browser.find_element_by_name('firstname')
fname.send_keys('Stanley')

lname = browser.find_element_by_name('lastname')
lname.send_keys('Nobody')

email = browser.find_element_by_name('email')
email.send_keys('a@b.c')

file_input = browser.find_element_by_css_selector('input[type="file"]')
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '2.2-3_empty.txt')
print(file_path)
file_input.send_keys(file_path)

button = browser.find_element_by_tag_name('button')
button.click()

time.sleep(10)

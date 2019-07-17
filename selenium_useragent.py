from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.whatsmyua.info/')

custom_ua_string = browser.find_element_by_id('custom-ua-string')
print(custom_ua_string.text)
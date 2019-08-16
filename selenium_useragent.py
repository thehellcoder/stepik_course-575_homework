from selenium import webdriver

def print_user_agent(browser_name):
    browser = None
    if browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        browser = webdriver.Chrome()
    browser.get('https://www.whatsmyua.info/')
    custom_ua_string = browser.find_element_by_id('custom-ua-string')
    print('[*] {} = {}'.format(browser_name, custom_ua_string.text))
    browser.quit()

if __name__ == '__main__':
    print_user_agent('chrome')
    print_user_agent('firefox')

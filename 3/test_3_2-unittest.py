import unittest
from selenium import webdriver

def signup(url):
        browser = webdriver.Chrome()
        browser.get(url)
        browser.implicitly_wait(5)

        first_name_input = browser.find_element_by_css_selector('div.first_block input.first')
        first_name_input.send_keys('Stanley')

        last_name_input = browser.find_element_by_css_selector('div.first_block input.second')
        last_name_input.send_keys('Nobody')

        email_input = browser.find_element_by_css_selector('div.first_block input.third')
        email_input.send_keys('a@b.c')

        submit_button = browser.find_element_by_tag_name('button')
        submit_button.click()

        result = browser.find_element_by_tag_name('h1').text
        browser.quit()
        return result

class TestSignup(unittest.TestCase):        
    def test_signup1(self):
        result = signup('http://suninjuly.github.io/registration1.html')
        self.assertIn('успешно', result, 'Signup failed')
        
    def test_signup2(self):
        result = signup('http://suninjuly.github.io/registration2.html')
        self.assertIn('успешно', result, 'Signup failed')

if __name__ == '__main__':
    unittest.main()

# Run me with pytest -v --tb=line test_3_4_parametrize.py
import time
import math
import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def answer():
    answer = math.log(int(time.time()))
    return str(answer)

@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestSuite():
    @pytest.mark.parametrize('num', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    def test_stepik_lesson_with_param(self, browser, answer, num):
        link = 'https://stepik.org/lesson/{}/step/1'.format(num)
        browser.get(link)
        browser.implicitly_wait(60)
        textarea = browser.find_element_by_tag_name('textarea')
        textarea.send_keys(answer)
        submit_button = browser.find_element_by_css_selector('.submit-submission')
        submit_button.click()
        result = browser.find_element_by_css_selector('.smart-hints__hint').text
        assert 'correct' in result.lower(), result

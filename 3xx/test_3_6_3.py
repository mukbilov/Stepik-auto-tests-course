import time
import math
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    number = [ 236905]#236895, 236896, 236897, 236898, 236899, 236903, 236904,

    @pytest.mark.parametrize("num", number)
    def test_link(self, browser, num):
        link = f"https://stepik.org/lesson/{num}/step/1"
        print(link)
        browser.get(link)
        time.sleep(3)
        answer = math.log(int(time.time() - 1.2))
        answer = str(answer)
        input_text = browser.find_element_by_css_selector("[class = 'textarea string-quiz__textarea ember-text-area ember-view']")
        input_text.send_keys(answer)
        button1 = browser.find_element_by_css_selector("[class = 'submit-submission']")
        button1.click()
        time.sleep(30)


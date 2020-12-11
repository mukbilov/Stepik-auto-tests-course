from selenium import webdriver
import unittest


class test_system(unittest.TestCase):
    def test_name(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(
            '[class="first_block"]>[class="form-group first_class"]>input[class="form-control first"] ')
        input1.send_keys("Adiz")
        input2 = browser.find_element_by_css_selector(
            '[class="first_block"]>[class="form-group second_class"]>input[class="form-control second"] ')
        input2.send_keys("Mukbilov")
        input3 = browser.find_element_by_css_selector(
            '[class="first_block"]>[class="form-group third_class"]>input[class="form-control third"]')
        input3.send_keys("mukbilov@mail.ru")
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", "should be welcom text")


if __name__ == "__main__":
    unittest.main()

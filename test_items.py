
link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_the_button(browser):
    browser.get(link)
    button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button.is_enabled() and button.is_displayed()


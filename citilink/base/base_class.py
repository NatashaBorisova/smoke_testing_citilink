import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url : " + get_url)


    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word : " + value_word)


    """Method scroll page"""

    def scroll_page(self, horizontal, vertical):
        X = horizontal
        Y = vertical
        self.driver.execute_script("window.scrollTo(X, Y)")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot("C:\\Users\\ILLUZIA\\PycharmProjects\\citilink\\screen\\" + name_screenshot)
        print("Screenshot: " + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good url : " + get_url)




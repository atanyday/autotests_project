import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    # Method current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    # Method asser url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Correct value url")

    # Method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Correct value word")

    # Method screenshot
    def save_screen(self):
        now_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('../screen/' + name_screenshot)
        print("Screenshot ready")
from selenium.webdriver.common.by import By


class Homepage:
    # URL
    URL = 'http://opencart.abstracta.us/index.php?route=common/home'

    # locators
    ADD_Cart1 = (By.XPATH, "//div[@class='row']//div[@class='row']//div[2]//div[1]//div[3]//button[1]")
    # ADD_Cart1 = (By.XPATH, "a")

    # initializer
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    # interaction method
    def click_add_button(self):
        click_add_button = self.browser.find_element(self.ADD_Cart1)
        click_add_button.click()

    def click_add_button(self):
        click_add_button = self.browser.find_element(self.ADD_Cart1)
        click_add_button.click()

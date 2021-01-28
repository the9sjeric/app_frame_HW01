from page.market import Market
from page.base import BasePage
from appium.webdriver.common.mobileby import By

class Quotation(BasePage):

    def goto_my_customer(self):
        pass

    def goto_market(self):
        self.find_click((By.XPATH, '//*[contains(@resource-id,"title_text") and @text="市场"]'))
        return Market(self.driver)

    def goto_mypage(self):
        pass
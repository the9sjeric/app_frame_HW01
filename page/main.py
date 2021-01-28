from page.base import BasePage
from page.quotation import Quotation
from appium.webdriver.common.mobileby import By


class MainPage(BasePage):

    def goto_quotation(self):
        self.find_click((By.XPATH, '//*[contains(@resource-id,"tab_name") and @text="行情"]'))
        return Quotation(self.driver)

    def goto_blacklist(self):
        # 手动制造黑名单页面
        self.driver.find_element(By.XPATH, '//*[contains(@resource-id,"action_message")]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@resource-id,"action_back")]').click()
        return self

    def goto_workspace(self):
        pass

    def goto_mypage(self):
        pass
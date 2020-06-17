# coding:utf-8
from pages.login_page2 import Login_element
class LoginTest:
    def __init__(self,driver):
        self.element = Login_element(driver)
        self.app = self.element.get_element
    def login(self,username,password):
        self.app.send_text(self.element.user_element(),username)
        self.app.send_text(self.element.password_element(),password)
        self.app.click(self.element.login_boot())
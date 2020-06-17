# coding:utf-8
from pages.login_page import LoginPage

class LoginHandle:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)
    def send_username(self,user,path):
        self.login_page.get_username_element(path).send_keys(user)

    def send_password(self,password,path):
        self.login_page.get_password_element(path).send_keys(password)

    def click_login_button(self,path):
        self.login_page.get_login_button_element(path).click()





# coding:utf-8
from common.get_by_local import GetByLocal

class LoginPage:
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)
    def get_username_element(self,path):
        return self.get_by_local.get_element(path,'username')

    def get_password_element(self,path):
        return  self.get_by_local.get_element(path,'password')

    def get_login_button_element(self,path):
        return self.get_by_local.get_element(path,'login_button')


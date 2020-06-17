# coding:utf-8
from common.Base import BaseApp
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.loger import Logger
path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(os.path.join(os.path.dirname(path),'config'),'appium.yaml')
class Login_element:
    def __init__(self,driver):
        self.log = Logger('element.py')
        self.driver = driver
        self.get_element = BaseApp(self.driver)
    def user_element(self):
        ''' 获取用户名元素'''
        self.log.info('正在获取用户名元素信息---------------------------------------')
        element = self.get_element.get_element(yaml_path,'LoginPage')['locators'][0]
        self.log.info('用户名元素信息为：%s'%element)
        return element

    def password_element(self):
        ''' 获取密码元素'''
        self.log.info('正在获取用户名元素信息-------------------------------------')
        element = self.get_element.get_element(yaml_path,'LoginPage')['locators'][1]
        self.log.info('密码元素信息为：%s'%element)
        return element

    def login_boot(self):
        ''' 获取登录按钮元素'''
        self.log.info('正在获取用户名元素信息-------------------------------------')
        element = self.get_element.get_element(yaml_path,'LoginPage')['locators'][2]
        self.log.info('登录按钮元素信息为：%s'%element)
        return element

    def toast(self,message):
        '''获取toast信息'''
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%message)
        element = WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        return element
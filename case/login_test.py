# coding:utf-8
from pages.login_page import LoginPage
import time
import os
import threading
from common.aa import Server
path  =os.path.dirname(os.getcwd())
# 获取到yaml文件路径
yaml_path = os.path.join(os.path.join(path,'config'),'element.yaml')
class BaseDriver:
    def login(self,driver):
        page =LoginPage(driver)
        time.sleep(8)
        # 获取用户名元素以及输入内容
        use = page.get_username_element(yaml_path)
        use.send_keys('1111')
        # 获取密码元素以及输入内容
        pas = page.get_password_element(yaml_path)
        pas.send_keys('22222')
        # 进行点击登录
        button = page.get_login_button_element(yaml_path)
        button.click()
if __name__ == '__main__':
    x = BaseDriver()
    server = Server()
    dev = Server().get_driver()
    t1 = threading.Thread(target=server.main)
    t1.start()
    time.sleep(60)
    aa = []
    for i in dev:
        devices = server.android_start(i)
        t2 = threading.Thread(target=x.login,args=(devices,))
        aa.append(t2)
    for j in aa:
        j.start()
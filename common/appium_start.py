# coding:utf-8
from appium import webdriver
from common.dos_cmd import Dos_adb
import os
from common.loger import Logger
log = Logger('anjing')
path = os.path.dirname(os.path.realpath(__file__))
appium_log = os.path.join(os.path.join(os.path.dirname(path),'logs'),'appium_log.txt')
desired_caps = {
             'platformName': 'Android',  # 测试版本
             'platformVersion': '5.1.1', # 系统版本
            "appPackage": "com.taobao.taobao",   # app包名
            'automationName':"uiautomator2",
            "appActivity": "com.ali.user.mobile.login.ui.UserLoginActivity",   # 启动launch Activity
            "noReset": True,  # 不清空数据
            "unicodeKeyboard": True,    # 使用Unicode编码方式发送字符串
            "resetKeyboard": True,      # 键盘隐藏起来
                                }

def start():
    '''
     启动appium
    '''
    adb = Dos_adb()
    devices = adb.get_device()[0]
    log.info('测试设备列表：%s'%devices)
    a = 'appium -p 4723 -U '+devices +' --log  %s' %appium_log
    log.info('输入adb命令，启动appium服务，输入命令如下：%s'%a)
    adb.get_adb(a)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver





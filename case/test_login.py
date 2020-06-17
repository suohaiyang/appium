from function.login import LoginTest
from common.appium_start import start
import unittest
import threading
import time
from common.loger import Logger
import warnings
warnings.simplefilter("ignore", ResourceWarning)
class BaseDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''启动apk'''
        cls.log = Logger('anjing')
        cls.log.info('app启动中')
        cls.driver = start()
        cls.log.info('app启动完成')
        cls.login = LoginTest(cls.driver)
    def test01(self):
        '''账号密码错误'''
        self.log.info('用例名称：账号密码错误，测试数据：账号名：11111，密码：22222,')
        self.login.login('11111','22222')
        element= self.login.element.toast('手机号')
        self.log.info('test01获取toast信息为：%s'%element)
        self.assertEqual(element,'请输入正确的手机号')
    def test02(self):
        '''账号密码错误1'''
        self.log.info('用例名称：账号密码错误1，测试数据：账号名：222，密码：33333,')
        self.login.login('2222','33333')
        element= self.login.element.toast('手机号')
        self.log.info('test02获取toast信息为：%s' %element)
        self.assertEqual(element,'请输入正确的号')

    @classmethod
    def tearDownClass(cls):
        '''退出APK'''
        cls.driver.quit()

if __name__ == '__main__':
    t1 = threading.Thread(target=start)
    t1.start()
    time.sleep(20)
    t2 = threading.Thread(target=unittest.main())
    t2.start()


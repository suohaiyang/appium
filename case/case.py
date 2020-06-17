from common.Base import BaseApp
from common.appium_start import start
from pages.login_page2 import Login_element
import unittest
import threading
import time
class BaseDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''启动apk'''
        cls.driver = start()
        cls.app = BaseApp(cls.driver)
        cls.element = Login_element(cls.driver)
    def test_01(self):
        '''账号密码错误'''
        self.app.send_text(self.element.user_element(),'1111')
        self.app.send_text(self.element.password_element(),'2222')
        self.app.click(self.element.login_boot())
        element = self.element.toast('手机号')
        self.assertIn(element,'请输入正确的手机号')
    def test_02(self):
        '''账号密码错误'''
        self.app.send_text(self.element.user_element(),'22222')
        self.app.send_text(self.element.password_element(),'33333')
        self.app.click(self.element.login_boot())
        element = self.element.toast('手机号')
        self.assertIn(element,'请输入正确的手机号')


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


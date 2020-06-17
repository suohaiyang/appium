from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.read_yaml import GetYaml
from common.loger import Logger
import os
path  =os.path.dirname(os.getcwd())
# 获取到yaml文件路径
jpg_path = os.path.join(os.path.join(path,'jpg'))
print(jpg_path)
class BaseApp:
    def __init__(self, driver):
        self.log = Logger('Base.py')
        self.driver = driver
    def find(self, locator):
        if not isinstance(locator, dict):
            self.log.error('定位参数locator传值不对，必须传入字典,如: {"name": "输入账号", "by": "id", "value": "xxx"}')
        if "name" in locator:
            self.log.info("正在操作元素名称\"%s\"" %locator['name']+",定位方法: %s-->%s"% (locator['type'], locator['value']))
        if locator["type"] == "id":
            value = locator["value"]
            element = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_id(value))
        elif locator["type"] == "android":
            value = locator["value"]
            element = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_android_uiautomator(value))
        elif locator["type"] == 'className':
            value = locator['value']
            element = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_element_by_class_name(value))
        elif locator["type"] == "text":
            value = "//*[@text='%s']" % locator["value"]
            _loc = ("xpath", value)
            element = WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(_loc))
        else:
            loc = (locator["type"], locator["value"])  # 元祖
            element = WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(loc))
        return element

    def get_element(self,path,key):
        '''读取元素'''
        yaml_data = GetYaml(path)
        local = yaml_data.get_data(key)
        return local

    def click(self, locator):
        '''点击元素'''
        el = self.find(locator)
        el.click()

    def send_text(self, locator, text):
        '''发送文本'''
        el = self.find(locator)
        el.send_keys(text)

    def screencap(self,png):
        self.driver.get_screenshot_as_file(jpg_path+'\\%s.png'%png)








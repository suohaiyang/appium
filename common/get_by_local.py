# coding:utf-8
from common.read_yaml import GetYaml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,path,key):
        # 获取到yaml地址，并进行读取器
        yaml_data = GetYaml(path)
        local = yaml_data.get_data(key)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_id(local_by))
                elif by == 'className':
                    element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_class_name(local_by))
                elif by == 'xpath':
                    element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_xptah(local_by))
                elif by == 'android':
                    element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_android_uiautomator(local_by))
                else:
                    loc = (by,local_by)  # 元祖
                    element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(loc))
                return element
            except:
                    return None
        else:
            return None


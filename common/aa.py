# coding:utf-8
# coding:utf-8
import time
from common.dos_cmd import Dos_adb
from common.read_yaml import GetYaml
import os
from appium import webdriver
import threading
import multiprocessing
path  =os.path.dirname(os.getcwd())
app = os.path.join(os.path.join(path,'config'),'app.yaml')
class Server():
    def __init__(self):
        self.adb = Dos_adb()
        self.yaml = GetYaml(app)
    def get_driver(self):
        '''获取设备列表'''
        devices_list = self.adb.get_device()
        return devices_list

    def get_dos(self):
        '''命令行启动appium'''
        result = self.yaml.get_data()
        dos_list = []
        android_list = []
        for j in result:
            port = j['port']
            devices = j['desired_caps']['deviceName']
            android_list.append(j['desired_caps'])
            for i in range(1):
                a = 'appium -p %s -U %s' %(port,devices)
                print(a)
                dos_list.append(a)
        return dos_list

    def get_commad(self):
        '''执行appium启动'''
        self.dos_list = self.get_dos()
        for i  in  self.dos_list:
            self.adb.get_adb(i)

    def get_android(self,devicesName):
        '''获取port和设备信息'''
        desired_caps = self.yaml.get_data()
        for i in desired_caps:
            if devicesName in i['devices']:
                port = i['port']
                desired_cap = i['desired_caps']
                return (port,desired_cap)

    def main(self):
        '''多线程启动'''
        multi_list = []
        for i in range(2):
            appium_server = multiprocessing.Process(target=self.get_commad)
            multi_list.append(appium_server)
        for j in multi_list:
            j.start()
        for j in multi_list:
            j.join()
        # thread_list = []
        # for i in range(2):
        #     appium_server = threading.Thread(target=self.get_commad)
        #     thread_list.append(appium_server)
        # for j in thread_list:
        #     j.start()
        # time.sleep(5)

    def android_start(self,deviceName):
        '''启动webdriver'''
        android = self.get_android(deviceName)
        driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % android[0], android[1])
        return driver

if __name__ == '__main__':
    xx = Server()
    xx.main()

    # devices = xx.get_driver()
    # print(devices)
    # for i in devices:
    #     xx.main()
    #     time.sleep(5)
    #     xx.android_start(i)




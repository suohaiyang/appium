# coding:utf-8
import os
class Dos_adb:
    def get_adb_result(self,command):
        '''
        :param command: Dos中输入内容
        :return: 返回解决内容
        '''
        adb_result = os.popen(command).read().split('\n')
        return adb_result

    def get_device(self):
        '''
        获取到设备信息
        '''
        xx = Dos_adb()
        devices = []
        result_list = xx.get_adb_result('adb devices')
        result = [x for x in result_list if x != '']
        if len(result)>1:
            for i in result:
                if 'List' in i:
                    continue
                de = i.split('\tdevice')
                devices.append(de[0])
            return devices
        else:
            return None
    def get_adb(self,command):
        '''
        执行adb 命令:
        '''
        os.system(command)
if __name__ == '__main__':
    x= Dos_adb()
    print(x.get_device())




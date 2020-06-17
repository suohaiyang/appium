# coding:utf-8

import logging,time
import os
# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path): os.mkdir(log_path)

class Logger(object):
    def __init__(self,name):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(name)s-%(levelname)s-%(message)s')
        # 创建一个FileHandler,存储日志文件
        fh = logging.FileHandler(self.logname, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.formatter)
        self.logger.addHandler(sh)

    def info(self,message):
        self.logger.info(message)

    def debug(self,message):
        self.logger.debug(message)

    def warning(self,message):
       self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def Fatal(self,message):
        self.logger.critical(message)


if __name__ == '__main__':
    log = Logger('Anjing')
    log.info('基础信息')
    log.debug('调试信息')
    log.warning('警告信息')
    log.error('错误信息')
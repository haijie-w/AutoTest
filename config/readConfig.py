# coning = utf-8
__author__ = 'Aimee'
import os
import configparser

#定位到config.ini文件
prjDir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(prjDir,"config.ini")

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()#创建configparser对象实例
        self.cf.read(config_path,encoding='UTF-8') #一启动就读取配置文件

    def get_email(self,name):
        value = self.cf.get("EMAIL",name)
        return value
    def get_http(self,name):
        value = self.cf.get("HTTP",name)
        return value
    def get_db(self,name):
        value = self.cf.get("DATABASE",name) 吧  
        return value

    def get_projectpath(self,name):
        value = self.cf.get('PROJECT',name)
        return value

if __name__ == "__main__":
    info = ReadConfig()
    print(info.get_projectpath('project_path'))

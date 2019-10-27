# -*-coding:utf-8 -*-
from src.config.VarConfig import *
import  configparser


#封装方法：从D:\JYH-1-AUTO\config\JYH_config.conf 读取配置
class Parse_JYH_Config(object):
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(account_dir,encoding='utf-8')
    def get_option(self,sectionName,option):
         return self.cf.get(section=sectionName,option=option)
    def get_items(self,sectionName):
        return  dict(self.cf.items(section=sectionName))

#封装方法：从D:\JYH-1-AUTO\page_element\page_element_workbench_pay.ini 读取配置
class Parse_ele_Config(object):
    def __init__(self,file_path):
        self.cf=configparser.ConfigParser()
        self.cf.read(file_path,encoding='utf-8')
    def get_option(self,sectionName,option):
         return self.cf.get(section=sectionName,option=option)
    def get_items(self,sectionName):
        return  dict(self.cf.items(section=sectionName))
if __name__=='__main__':
    G=Parse_JYH_Config()
    print(G.get_items('account_info'))
    print(G.get_option('account_info','station_username'))
    print(G.get_option('account_info', 'station_password'))
    H=Parse_ele_Config()
    print(H.get_option('workbench','workbench_text'))

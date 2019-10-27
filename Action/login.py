# -*-coding:utf-8 -*-
import requests
import untils
from untils import find
from untils import  helper
from  untils.config_handler import *
from untils import PageAction
from untils.PageAction import  *
from selenium.webdriver import *
import selenium

def login():
    # helper.open_browser('chrome')
    # helper.open_url()
    #从配置读取用户信息
    userName=Parse_JYH_Config().get_option(sectionName='account_info',option='station_username')
    #输入用户名
    PageAction.input_string(read_file.get_option('login','userName'),content=userName)
    password = Parse_JYH_Config().get_option(sectionName='account_info', option='station_password')
    # 输入密码
    PageAction.input_string(read_file.get_option('login','password'), content=password)
    # 输入验证码
    txtCode = Parse_JYH_Config().get_option(sectionName='account_info', option='txtCode')
    PageAction.input_string(read_file.get_option('login','txtCode'), content=txtCode)
    #点击登录
    PageAction.click(read_file.get_option('login','login_button'))
    #校验页面元素,左侧侧边栏文本包含'工作台'
    find.getElement(read_file.get_option('login','workbench'),seconds=14)
    print('账号%s登录成功！'%(userName))


if __name__ =='__main__':
    login()
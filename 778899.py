import os,time, selenium
from  selenium  import webdriver
from untils.helper import *
import sys
# o=os.popen('tasklist /fi "imagename eq chrome.exe"')
# l="avb\\src"
# # print(l)
# # print(l.replace("\\src", ""))
# print(sys.argv[0])
import sys
# print(sys.path)
import os

#获取项目路径下的目录
# os.chdir('D:\JYH-AUTO')
# print(os.getcwd())
#打印出项目路径下的目录
for file in os.listdir(os.getcwd()):
     print(file)
# -*-coding:utf-8 -*-
from src.config.VarConfig import *
import  os
from untils.config_handler import *
from selenium import webdriver
import time,selenium

driver=None

# 浏览器启动
def open_browser(browser_name,*args):
    global  driver
    try:
        if browser_name.lower().strip() == 'chrome':
            kill_chrome_process()
            option=selenium.webdriver.ChromeOptions()
            option.add_argument("--start-maximized")
            # option.add_argument("--disable-web-security")
            # option.add_argument('--profile-directory=Default')
            # option.add_argument("--test-type")
            # option.add_argument("--user-data-dir=" + str(os.path.abspath("user.home")) + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
            # prefs = {"credentials_enable_service": False, "credentials_enable_service": False}
            # option.add_experimental_option("prefs", prefs)
            option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            driver= selenium.webdriver.Chrome(chrome_options=option, executable_path=chrome_driver_path)
        elif browser_name.lower().strip() == 'ie':
            driver = webdriver.Ie(executable_path=Ie_driver_path)
        else:
            driver = webdriver.Firefox(executable_path=Firefox_driver_path)
        return driver
    except Exception as e:
        print('浏览器启动失败')

# 获取selenium对象
def get_selenium():
    return driver

# 打开网址
def open_url(myurl=None,*args): #url参数可带可不带，带就指定，不带默认取D:\JYH-1-AUTO\config\JYH_config.conf 目录下base_url_info
    if myurl:
        url=myurl
    else:
        url=Parse_JYH_Config().get_option('base_url_info','url')
    try:
        get_selenium().get(url)
    except Exception as e:
        raise e

#启动浏览器前先杀已存的相同进程，保证环境干净
def kill_chrome_process():
    killed=False
    try:
        while not killed:
            #os.popen(command[, mode[, bufsize]])   从一个 command 打开一个管道
            o=os.popen('tasklist /fi "imagename eq chrome.exe"')
            # 通过os.popen()返回的是file  read的对象，对其进行读取read()的操作可以看到执行的输出
            text=str(o.read())
            if "chrome.exe" in text:
                os.popen('taskkill /im chrome.exe /f')
                time.sleep(1)
            else:
                killed=True  #用于跳出while循环
        killed=False
        while not killed:
            o=os.popen('tasklist /fi "imagename eq chromedriver.exe"')
            text=str(o.read())
            if "chromedriver.exe" in text:
                os.popen('taskkill /im chromedriver.exe /f')
                time.sleep(1)
            else:
                killed=True   #用于跳出while循环
    except:
        print("进程chrome.exe 或者 chromedriver.exe不存在")


# 关闭释放selenium对象，关闭driver和chrome进程
def release_selenium():
    global driver
    try:
        driver.quit()  #关闭的时候尽量用quit而不用close，close只会关闭当前页面，quit会退出驱动并且关闭所关联的所有窗口，最后执行完以后就关闭。
        kill_chrome_process()
    except Exception as e:
        raise e


# 定义pytest调试方法参数
def get_pytest_param(file_name, option=None):
    html_file = get_src_path() + "\\report.html"
    html_file = html_file.replace("\\src", "")
    file_name = file_name + " --html=" + html_file + " --driver Chrome --driver-path " + get_chromedriver_path()
    if option:
        file_name = file_name + " " + option
    print(file_name)
    return file_name

if __name__ =="__main__":
    print(open_browser('chrome'))
    print(driver)


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from untils.helper import *
from untils import  helper
from untils import PageAction
from selenium.webdriver import  ActionChains
from untils.PageAction import *

#五秒等待时间，等待某个元素出现
def getElement1(localType,localExpression,seconds=None):
    if not seconds:
        seconds =5
    try:
        element_obj=WebDriverWait(get_selenium(), seconds).until(lambda x:x.find_element(by=localType,value=localExpression))
        return element_obj
    except Exception as e:
        raise  e




#默认5秒等待时间，等待某个元素出现
def getElement(localtion,seconds=None):
    time.sleep(1)
    if isinstance(localtion,str) and ',' in localtion:
        selector_by = localtion.split(',')[0]
        localExpression = localtion.split(',')[1]
        # print(selector_by,localExpression)
        if not seconds:
            seconds =5
        if selector_by=='x' or selector_by== 'xpath':
            localType='xpath'
        elif selector_by=='i' or selector_by== 'id':
            localType='id'
        elif selector_by=='n' or selector_by== 'name':
            localType='name'
        elif selector_by=='t' or selector_by== 'tag name':
            localType='tag name'
        elif selector_by == "l" or selector_by == 'link':
            localType = 'link text'
        elif selector_by == "p" or selector_by == 'partial_link_text':
            localType = 'partial link text'
        elif selector_by == "c" or selector_by == 'css_selector':
            localType='css selector'
        elif selector_by == "c" or selector_by == 'class_name':
            localType = 'class selector'
        else:
            raise NameError("Please enter a valid type of targeting elements.")
    try:
        ele = WebDriverWait(get_selenium(), seconds).until(
        lambda x: x.find_element(by=localType, value=localExpression))
        return ele
    except Exception as e:
        raise PageAction.JYHException("找不到元素")
    else:
        print('当前输入错误,要求文本类型且带逗号分隔符')
#
# #五秒等待时间，等待某个标签元素出现
# def getElement_tag_name(tagName,seconds=None):
#     if not seconds:
#         seconds =5
#     try:
#         tag_name_obj=WebDriverWait(get_selenium(),seconds).until(lambda x:x.find_element_by_tag_name(tagName))
#         return tag_name_obj
#     except Exception as e:
#         raise e

def getElemtns(localType,localExpression,driver=None):
    try:
        elements=WebDriverWait(open_browser('chrome'),7).until(lambda x:x.find_element(by=localType,value=localExpression))
        return elements
    except Exception as e:
        raise e

 # 等待菜单到可点击状态
def elementToBeClickable(localType,localExpression):
    try:
        get_selenium().execute_script("arguments[0].scrollIntoView(true);", getElement(localType,localExpression))
        WebDriverWait(get_selenium(),0.7).until(EC.element_to_be_clickable((localType,localExpression)))
        return True
    except Exception as e:
        raise  e






if __name__=='__main__':
    helper.open_browser('chrome')
    helper.open_url()
    # print(getElement(localType='id', localExpression="userName"))
    PageAction.input_string(locatorMethod="id", localExpression="userName", content="1223")
    # Action.input_string(locatorMethod="id",localExpression="kw",content="123")
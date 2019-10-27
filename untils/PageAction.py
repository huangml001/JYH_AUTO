from untils.find import *
from untils.helper import *
from src.config.VarConfig import *
from untils.FormatTime import *
from untils.DirandFile import *
from untils.helper import *
from untils import  helper
from untils import  find
from untils import KeyboardUlit
from selenium.webdriver import  ActionChains




# 从D:\JYH-1-AUTO\page_element\page_element_workbench_pay.ini 读取配置
read_file= Parse_ele_Config(workbench_ele_dir)

#获取元素指定的属性内容
def getelement_attribute(localtion,attr,*args):
    try:
        attr_value=find.getElement(localtion).get_attribute(attr)
        return attr_value
    except Exception as e:
        raise e

# 获取元素文本内容
def getelement_text(localtion, *args):
    try:
        text_value = find.getElement(localtion).text
        return text_value
    except Exception as e:
        raise e


# 直接拖动到底部
def roll_bottom():
    get_selenium().execute_script("window.scrollTo(0,document.body.scrollHeight)")



#获取元素对象输入内容
def input_string(localtion,content,*args):
    try:
        ele_object=find.getElement(localtion)
        ele_object.clear()
        ele_object.send_keys(content)
    except Exception as e:
        raise e


# 获取元素对象点击
def click(localtion,*args):
    try:
        ele_object=find.getElement(localtion)
        ele_object.click()
    except Exception as e:
        raise e

# def click1(localType,localExpression,*args):
#     try:
#         ele_object=find.getElement(localType,localExpression)
#         ele_object.click()
#     except Exception as e:
#         raise e

# 定位svg点击元素
def click_SvgelementXpath(localtion, seconds=None):
    try:
        Svgelement=find.getElement(localtion)
        action = ActionChains(get_selenium())
        action.click(Svgelement).perform()
    except Exception as e:
        raise e


#按回车键,模拟enter键
def press_enter_key(*args):
    KeyboardUlit.KeyboardKeys().oneKey('enter')




# 预期内容进行断言
def assert_word(expected_word ,*args):
    pause(2)
    try:
        assert expected_word in get_selenium().page_source
        return True
    except AssertionError as e:
        print('页面找不到"%s"'%(expected_word))
        return False
    # except Exception as e:
    #     raise e
    #     return False
    #     Action.pause(3)

# 定义JYH系统异常
class JYHException(Exception):
    print(Exception)
    pass

# 等待
def pause(seconds,*args):
    time.sleep(float(seconds))

#定位其中的iframe，并切进去
def enter_frame(locatorMethod,locatorExpression):
    global driver
    try:
        ele_object=getElement(driver,localType=locatorMethod,localExpression=locatorExpression)
        driver.switch_to.frame(ele_object)
    except Exception as e:
        raise  e
        print('can not enter frame')

#从frame中切回主文档
def default_content():
    global  driver
    driver.switch_to.default_content()

# 截图，正常,命名方式：工程路径，年月日时分秒
def capture_screen(driver=None):
    if not driver:
        driver=helper.get_selenium()
    PicPathAndName = os.path.join(createCurrentDateDir(), getCurrentTime() + '.png')
    try:
        # get_screenshot_as_file和save_screenshot
        # save_screenshot()方法，参数是文件名称，截取的屏幕截图会保存在当前的目录下，即与模块在同一个路劲下
        # get_screenshot_as_file(filename)方法也是获取屏幕截图，不过保存的是绝对路劲，与save_screenshot()方法不同的是，它的参数是带有完整的路劲
        driver.get_screenshot_as_file(filename=PicPathAndName)
        time.sleep(2)
    except Exception as e:
        raise  e
    else:
        return PicPathAndName


# 异常截图,命名方式：工程路径，年月日时分秒
def capture_error_screen(driver=None):
    if not driver:
        driver=helper.get_selenium()
    PicPathAndName = os.path.join(createErrCurrentDateDir(), getCurrentTime() + '.png')
    try:
        driver.get_screenshot_as_file(filename=PicPathAndName)
        time.sleep(2)
    except Exception as e:
        raise  e
    else:
        return PicPathAndName

def create_report_dir():
    report_Folder = createDir(report_path, getCurrentDate())
    report_file_name = os.path.join(report_Folder, getCurrentTimeformat())
    return report_file_name



if __name__=='__main__':
    # # print(driver)
    # helper.open_browser('chrome')
    # helper.open_url()
    # print(getElement(localType='id', localExpression="userName"))
    # input_string(locatorMethod=id, localExpression="userName", content=str('userName'))
    import selenium.webdriver
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    capture_screen(driver=driver)

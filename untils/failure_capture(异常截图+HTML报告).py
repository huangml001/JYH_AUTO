# -*-coding:utf-8 -*-
#截图异常场景
from selenium import webdriver
import unittest,traceback,time,os
from  FileUtil import creatDir
from HTMLTestRunner import HTMLTestRunner
#创建存放异常截图的目录，并得到本次实例中存放图片目录的绝对路径，并且作为全局变量，以供本次所有测试用例调用
picDir=creatDir()
print(os.path.join(os.getcwd(), 'report.html'))
def takeScreenshot(driver,savePath,picName):
    #封装截屏方法，构造jp截图路径及图片名，windows默认gbk编码，而传入图片名为utf-8，所以需要编码
    picPath=os.path.join(savePath,str(picName)+'.png')
    print(1,picPath)
    try:
        #调用webdriver
        driver.get_screenshot_as_file(picPath)
    except Exception as e:
        print(traceback.print_exc())

class TestFailCaptureScreen(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def testSoGouSearch(self):
        url='http://www.sogou.com'
        self.driver.get(url)
        try:
            self.driver.find_element_by_id('query').send_keys('光荣')
            self.driver.find_element_by_id('stb').click()
            time.sleep(3)
            #
        #     self.assertTrue('1223' in self.driver.page_source,msg='1223在界面没找到')
        # except AssertionError as e:
        #     print(e)  #e=Flase is not true:1223在界面没找到,  切割提取冒号后的文本内容
        #     takeScreenshot(self.driver,picDir,str(e).split(':')[1])#切割提取冒号后的文本内容
        except Exception as e:
            print(traceback.print_exc())
            takeScreenshot(self.driver, picDir, str(e).split(':')[1])
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    # unittest.main()
    testsuit=unittest.TestSuite()
    testsuit.addTest(TestFailCaptureScreen('testSoGouSearch'))
    fp=open(os.path.join(os.getcwd(),'report001.html'),'wb')
    runner=HTMLTestRunner(stream=fp,title='report001',description='drtail look')
    runner.run(testsuit)
    fp.close()


# -*-coding:utf-8 -*-
import os

#项目目录
#os.path.dirname(os.path.dirname(__file__))--->D:/JYH-AUTO/src
#D:/JYH-AUTO/sr的目录-->D:/JYH-AUTO/
project_path=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# window下的目录都是\隔开,所以需要替换
project_path=project_path.replace('/',"\\")
# print(project_path)

# 正常截图的目录
screenPicDir=os.path.join(project_path,'ScriptPictures\CapturePicture')
print('screenPicturesDir',screenPicDir)

#异常截图的目录
screenErrPicDir=os.path.join(project_path,'ScriptPictures\ErrorPicture')



# D:\JYH-1-AUTO\JYH_config.conf
account_dir=os.path.join(project_path,'src\config\JYH_config.conf')
print(account_dir)

workbench_ele_dir=os.path.join(project_path,'page_element\page_element_workbench_pay.ini')
print(workbench_ele_dir)
#D:\JYH-1-AUTO\page_element\page_element_workbench_pay.ini

chrome_driver_path=os.path.join(project_path,'src\common\chromedriver.exe')


Ie_driver_path='C:\Python36\Scripts\IEDriverServer.exe'

report_path=os.path.join(project_path,'report')



if __name__ =='__main__':
    print('pass')
    project_path =os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(project_path)
    print(report_path)




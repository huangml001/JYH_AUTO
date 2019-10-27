import os
from src.config.VarConfig import *
from untils.FormatTime import *
import time

def createDir(path,dirName):
    dirPath=os.path.join(path,dirName)
    print(dirPath)
    if os.path.exists(dirPath):
        pass
    else:
        os.mkdir(dirPath)
    time.sleep(2)
    return dirPath


# 创建截图存放的目录,screenPicturesDir下创建以当前日期为命名的文件夹目录
def createCurrentDateDir():
    dirName = os.path.join(screenPicDir, getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:
        pass
    return dirName  # 需注意:覆盖if/else返回值都=dirname，否则影响其他模块的调用拼接

# 创建截图存放的目录,screenPicturesDir下创建以当前日期为命名的文件夹目录
def createErrCurrentDateDir():
    dirName = os.path.join(screenErrPicDir, getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:
        pass
    return dirName  # 需注意:覆盖if/else返回值都=dirname，否则影响其他模块的调用拼接

if __name__=='__main__':
    pass
    report_Folder=createDir(report_path, getCurrentDate())
    report_file_name=os.path.join(report_Folder,getCurrentTime())
    print(report_file_name)
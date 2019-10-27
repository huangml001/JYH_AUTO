import time
def getCurrentTime():
    # 返回当前年月日时分秒
    return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())

def getCurrentDate():
    # 返回当前年-月-日
    return time.strftime("%Y-%m-%d", time.localtime())

def getCurrentTimeformat():
    # 返回当前年月日时分秒
    return time.strftime('%Y%m%d%H%M%S',time.localtime())


if __name__=='__main__':
    pass
    print(getCurrentTimeformat())
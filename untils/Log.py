# -*-coding:utf-8 -*-
import logging
import logging.config
from  src.config.VarConfig import *


#project_path来源于 ProjectVar.var
Log_path=os.path.join(project_path,'src\config\Logger.conf')
logging.config.fileConfig(Log_path)
logger=logging.getLogger('example01')

#日志配置文件，多个logger，每个logger，指定不同的handler
#handler：设定日志输出行的格式
#handler:以及设定写到日志到文件（是否回滚）？还是到屏幕
#handler：打印日志的级别

def debug(message):
    #打印debug级别的日志方法
    #详细信息，一般只在调试问题时使用
    print('debug')
    logger.debug(message)

def warning(message):
    # 打印warning级别的日志方法
    #某些没有预料到的事件的提示，或者在将来可能会出现的问题提示。例如：磁盘空间不足。但是软件还是会照常运行
    print('warning')
    logger.warning(message)

def info(message):
    # 打印info级别的日志方法,由于更严重的问题,软件已不能执行一些功能
    print('info')
    logger.info(message)

def error(message):
    # 打印error级别的日志方法,由于更严重的问题，软件已不能执行一些功能
    print('error')
    logger.info(message)


if __name__=='__main__':
    debug('hi')
    info('hml')
    warning('wzhim')





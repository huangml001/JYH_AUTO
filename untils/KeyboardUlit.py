# -*-coding:utf-8 -*-
import win32api
import win32con
from untils import ClipboardUlit

class KeyboardKeys(object):
    #模拟键盘按键类,参考虚拟键Vk大全
    VK_CODE={'enter':0x0D,'ctrl':0x11,'v':0x56,'tab':0X09,'shift':0x10,'ALT':0x12,'Delete':0x2E,'Insert':0x2D }

    @staticmethod
    def keyDown(keyName):
        # 按下按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName],0,0,0)

    @staticmethod
    def keyUp(keyName):
        # 释放按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0,win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key): #对前面函数的调用
        #模拟单个按键hello world
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)


    @staticmethod
    def twoKeys(key1,key2): #对前面函数的调用
        # 模拟两个组合键
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key2)
        KeyboardKeys.keyUp(key1)

if __name__=='__main__':
    from selenium import webdriver
    from util.ClipboardUlit import *
    import time
    Clipboard.setText('hello world')
    time.sleep(3)
    KeyboardKeys.twoKeys('ctrl','v')
    KeyboardKeys.oneKey('tab')



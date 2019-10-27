# -*-coding:utf-8 -*-
# -*-coding:utf-8 -*-
import pytest
import sys,os
sys.path.append('../')  # 新加入的
sys.path.append(os.getcwd())
print(sys.path)
os.chdir('D:\JYH-AUTO\Action')
sys.path.append('D:\JYH-AUTO\Action')
sys.path.append(pytest)
from Action import login
# os.chdir('D:\JYH-AUTO\untils')
# sys.path.append('D:\JYH-AUTO\untils')
from untils import helper
from untils.PageAction import *



@pytest.fixture(scope="function")
def setup_module():
    helper.open_browser('chrome')
    helper.open_url()
    login.login()
    yield
    helper.release_selenium()

if __name__ =='__main__':
    pytest.main()



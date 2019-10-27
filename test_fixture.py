# -*-coding:utf-8 -*-
#test_fixture.py
import pytest

@pytest.fixture(scope='workbenck')
def open():
    print('打开浏览器,并且打开百度首页')
    yield
    print('执行teardown！')
    print('最后关闭浏览器')

def test_s1(open):
    '''如果第一个用例异常了，不影响其他的用例执行'''
    raise NameError
    print('用例1：搜索pthon01')

def test_s2(open):
    print('用例2：搜索pthon02')

def test_s3(open):
    print('用例3：搜索pthon03')

if __name__ == "__main__":
    import sys
    filename=sys.argv[0]
    pytest.main(['-v','test_fixture.py','--html=%s/report.html' %(filename)])


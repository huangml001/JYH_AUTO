# -*-coding:utf-8 -*-
# 模块中的方法
import pytest
def setup_module():
    print("setup_module：整个.py模块只执行一次")

def teardown_module():
    print("teardown_module：整个test_module.py模块只执行一次")

def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


# 测试模块中的用例1
@pytest.mark.must
def test_1():
    print("正在执行测试模块----test_one")
    x = "this"
    assert 'h' in x


# 测试模块中的用例2
def test_2():
    print("正在执行测试模块----test_two")
    x = "hello"
    # assert hasattr(x, 'check')
    # assert 'h' in x
    assert 'L' in x

# 测试类
class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def setup(self):
        print("setup：每个用例开始前都会执行")

    def teardown(self):
        print("teardown：每个用例结束后都会执行")

    def test_4(self):
        print("正在执行测试类----test_four")
        x = "hello"
        assert 'g' in x

    def test_3(self):
        print("正在执行测试类----test_three")
        x = "this"
        assert 'h' in x




if __name__ =="__main__":
    from src.config.VarConfig import *
    from collections import namedtuple
    import venv
    pass
    # pytest .main(test_passing())
    # pytest .main('test_by.py')
    # pytest.main(["-s", "test_by.py"])
    # pytest.main(["-v", "test_by.py","--ff"])
    # pytest.main(['-v','-k','_4'])
    # # pytest -v test_by.py --html=project_path
    # pytest.main(["-q", "test_by.py::test_1"])
    # pytest.main(["-k", "_4 --collect-only" ])
    # pytest.main(["-k", "_4 "])
    # pytest.main(['-v','-k','_4'])
    # pytest.main(['-x','test_by.py','--maxfail=2','--tb=no'])






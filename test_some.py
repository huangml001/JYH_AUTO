# -*-coding:utf-8 -*-
import pytest

def test_7():
    print("正在执行测试类----test_seven")
    x = "this"
    assert 'h' in x

# @pytest.mark.must
# def test_8():
#     print("正在执行测试类----test_eight")
#     x = "hello"
#     assert hasattr(x, 'check')

if __name__ =="__main__":
    pytest.main(['-v','test_some.py::test_7'])
    # pytest.main(['-s','-m=must'])

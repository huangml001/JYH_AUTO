# -*-coding:utf-8 -*-
import requests
import pytest
import is_leap_year
#let.py

class TestAssert():
    @pytest.mark.parametrize('task',[Task('sleep','done=True',Task('wake','brian'))])
    @pytest.mark.xfail(raises=ValueError)
    def test_a(self):
        is_leap_year.is_leap_year(-100)
if __name__ =="__main__":
    pytest.main(['-v','let.py'])
# -*-coding:utf-8 -*-
# def test_Cash_rechange():
import pytest
from untils import helper
from test_script.workbenck import login
from untils.PageAction import *

@pytest.fixture(scope="function")
def setup_module():
    helper.open_browser('chrome')
    helper.open_url()
    login.login()
    yield
    helper.release_selenium()

if __name__ =='__main__':
    # pass
    pytest.main(
    ['-s','-q','--html=%s_workbench_pay_report.html'%(create_report_dir()),
     '--alluredir=%s_report'%(create_report_dir())])




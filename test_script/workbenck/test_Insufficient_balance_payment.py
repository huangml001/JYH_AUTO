# -*-coding:utf-8 -*-
from Action import login,enter_workbench
from untils import find
from untils import PageAction
import random
from untils.Log import *
import pytest
from untils.config_handler import *
import allure

@pytest.mark.smoke
@allure.MASTER_HELPER.story('Balance_payment')
#汽油余额收款-不使用优惠券-加油金额>余额,预期:余额不足，支付失败
def test_Insufficient_balance_payment(setup_module):
    enter_workbench.workbench_payment() #输入手机号码，
    enter_workbench.Balance_payment_click()  # 支付方式按钮：余额支付
    enter_workbench.input_oilgunNo(enter_workbench.get_diesegunNo())  # 输入汽油枪号
    #[0::2]-->取奇数位包含列表末位，[0:-1:2]-->取奇数位不包含末位
    before_dieselBalance,before_commonlBalance=enter_workbench.workbench_inputPhone()[0::2] #加油前-获取汽油余额+通用余额
    if not (before_dieselBalance and before_commonlBalance):
        oilPrice=random.randint(2,10)
    else:
        oilPrice=int(float(before_dieselBalance)+float(before_commonlBalance)+1) #加油金额>余额
    enter_workbench.input_oilPrice(oilPrice)  #输入加油金额
    enter_workbench.clear_coupon()
    # 获取提交订单时计算的实收金额
    receivepayment=enter_workbench.get_receivepayment()
    print('实收金额:',receivepayment)
    # 获取提交订单时计算的优惠金额
    discount = enter_workbench.get_discount()
    print('提交订单时计算的优惠金额', discount)
    PageAction.capture_screen()
    # 收款操作
    PageAction.roll_bottom()
    enter_workbench.click_pay()
    if PageAction.assert_word('余额支付失败'):
        print('余额不足支付失败，与预期一致')
        enter_workbench.close_fail_pay_Popup()
        enter_workbench.close_payment_windows()
    else:
        PageAction.assert_word('余额支付成功')
        enter_workbench.close_payment_windows()
        print('余额不足不该支持成功，与预期不一致')
        error('余额不足不该支持成功，与预期不一致')


if __name__ == '__main__':
    pass









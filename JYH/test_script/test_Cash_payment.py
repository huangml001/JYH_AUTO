from Action import login,workbench_payment,enter_workbench
from untils import find
from untils import PageAction,helper
import random
from untils.Log import *
import pytest

#现金收款

def test_cash_payment(setup_module):
    enter_workbench.workbench_payment()  # 输入手机号码，
    enter_workbench.workbench_inputPhone()
    enter_workbench.input_oilgunNo(enter_workbench.get_diesegunNo())
    oilPrice=round(random.random()*100,2) #加油金额随机数字，保留2个小数位
    enter_workbench.input_oilPrice(oilPrice) #输入加油金额
    enter_workbench.clear_coupon()
    # 获取提交订单时计算的实收金额
    receivepayment = enter_workbench.get_receivepayment()
    print('实收金额:', receivepayment)
    # 获取提交订单时计算的优惠金额
    discount = enter_workbench.get_discount()
    print('提交订单时计算的优惠金额', discount)
    # enter_workbench.input_cash_receipt()
    Amount_Collected=enter_workbench.get_cash_receipt()
    print('提交订单时计算的收款金额', Amount_Collected)
    PageAction.capture_screen()
    enter_workbench.Cash_payment_click()
    enter_workbench.click_pay()
    if PageAction.assert_word('现金支付成功'):
        enter_workbench.close_success_pay_Popup()
        enter_workbench.close_payment_windows()
        print('现金支付流程成功')
    else:
        PageAction.assert_word('现金支付失败')
        enter_workbench.close_fail_pay_Popup()
        enter_workbench.close_payment_windows()
        print('现金支付流程失败')
        error('现金支付流程失败')


if __name__ == "__main__":
    pytest.main(['--html=report.html'])



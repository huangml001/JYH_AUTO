from Action import login,enter_workbench
from untils import find
from untils import PageAction,helper
import random
from untils.Log import *
from untils.config_handler import *
import pytest
import allure
from untils.PageAction import *

#汽油余额收款-不使用优惠券
@allure.MASTER_HELPER.story('balance_payment')
def test_balance_payment(setup_module):
    try:
        enter_workbench.workbench_payment() #输入手机号码，
        enter_workbench.Balance_payment_click()  # 支付方式按钮：余额支付
        enter_workbench.input_oilgunNo(enter_workbench.get_diesegunNo())  # 输入汽油枪号
        # 加油前-获取汽油余额和通用余额
        before_dieselBalance, before_commonlBalance = enter_workbench.workbench_inputPhone()[0::2]
        print('加油前-获取汽油余额和通用余额',before_dieselBalance, before_commonlBalance)
        if float(before_dieselBalance)>0:
            oilPrice=round((float(before_dieselBalance)/8)*100/100.0,2) #取加油金额=汽油余额的1/4
        elif float(before_commonlBalance)>0:
            oilPrice = round((float(before_commonlBalance)/8)*100/100.0,2)  # 取加油金额=通用余额的1/4

            # oilPrice=0.1
            enter_workbench.input_oilPrice(oilPrice)  #输入加油金额
            enter_workbench.clear_coupon()
            # 获取提交订单时计算的实收金额
            receivepayment=enter_workbench.get_receivepayment()
            print('实收金额:',receivepayment)
            # 获取提交订单时计算的优惠金额
            discount = enter_workbench.get_discount()
            print('提交订单时计算的优惠金额', discount)
            # PageAction.capture_screen()
            # 收款操作
            PageAction.roll_bottom()
            enter_workbench.click_pay()
            if PageAction.assert_word('余额支付成功') ==True:
                enter_workbench.close_success_pay_Popup()
                #断言部分： map(lambda x :float(x) ,L)
                Balance_list=enter_workbench.workbench_inputPhone()  #返回list包含 会员各种类型的余额文本
                print('Balance_list',Balance_list)
                after_dieselBalance, after_gaslBalance, after_commonlBalance = map(lambda x:float(x),Balance_list) #金额文本转成浮点金额
                except_remain_Balance = round((((float(before_dieselBalance) -oilPrice ) * 100) / 100.0),2)  # 预期剩余汽油余额
                print('原汽油余额:%s,应收金额:%s,预期剩余汽油金额:%s' % (before_dieselBalance, receivepayment, except_remain_Balance))
                # 断言会员余额加油前后变化
                if not except_remain_Balance == after_dieselBalance:
                    PageAction.capture_error_screen()
                    error('实际剩余汽油余额: %s 跟预期剩余汽油余额: %s不一致'%(after_dieselBalance,except_remain_Balance,))
                enter_workbench.close_payment_windows()
                payed = enter_workbench.get_order_realpay()
                print('订单记录的实收金额：', payed)
                if not receivepayment == payed :
                    PageAction.capture_error_screen()
                    error('订单记录的实收金额:%s与付款实付金额:%s不一致'%(payed,receivepayment))
                order_discount = enter_workbench.get_order_discount()
                print('订单记录的优惠金额：', order_discount)
                if not order_discount == discount:
                    PageAction.capture_error_screen()
                    error('订单的优惠金额:%s与付款优惠金额:%s不一致' %(order_discount,discount))
            else:
                PageAction.assert_word('余额支付失败')
                print('余额支付失败')
                enter_workbench.close_fail_pay_Popup()
                enter_workbench.close_payment_windows()
                error('余额支付失败')
        else:
            print('通用余额,汽油余额都不足无法进行余额支付')
            PageAction.capture_error_screen()
            error('通用余额,汽油余额都不足无法进行余额支付')
    except Exception as e:
        raise e
        print('过程执行失败')

if __name__ == '__main__':
    pass
    # pytest.main(['-s','test_Balance_payment.py','--html=%s_workbench_pay_report.html'%(create_report_dir())])
    # pytest.main(['-s','test_Balance_payment.py','--html=%s_workbench_pay_report.html'%(create_report_dir())
    #                 ,'--alluredir=%s_allure_result'%(create_report_dir())])
    # pass









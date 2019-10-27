from Action import login,enter_workbench
from untils import find,config_handler
from untils import PageAction,Table
import random


#收款-现金汽油-不使用优惠券
def Cash_payment():
    enter_workbench.workbench_payment()
    dieselBalance,gaslBalance,commonlBalance=enter_workbench.workbench_inputPhone()
    # 定位枪号元素且输入汽油枪号10
    enter_workbench.input_oilgunNo(enter_workbench.get_diesegunNo())
    #加油金额
    price=round(random.uniform(10, 200)*100/100.0 , 2)  #10-200之间四舍五入取两个小数位
    print('输入加油金额:',price)
    #输入加油金额
    enter_workbench.input_oilPrice(price)
    # 清空优惠券
    enter_workbench.clear_coupon()
    #获取提交订单时计算的实付金额
    receipt=enter_workbench.get_receiptpaymoney()
    print('提交订单时计算的实付金额', receipt)
    # 获取提交订单时计算的优惠金额
    discount=enter_workbench.get_discount()
    print('提交订单时计算的优惠金额',discount[0:-1])
    #收款操作
    enter_workbench.click_pay()
    PageAction.assert_word('现金支付成功')
    PageAction.click(locatorMethod='xpath',localExpression="//span[.='确定[Enter]']/parent::*")
    PageAction.pause(3)
    str_dieselBalance, str_gaslBalance, str_commonlBalance = enter_workbench.workbench_inputPhone()
    #断言会员余额加油前后没变化->现金支付成功
    if dieselBalance==str_dieselBalance and gaslBalance==str_gaslBalance and commonlBalance==str_commonlBalance:
        print('现金支付成功后会员余额不变与预期一致')
    enter_workbench.close_payment_windows()
    payed=enter_workbench.get_order_realpay()
    print('订单记录的实收金额：',payed)
    if receipt==payed:
        print('订单记录的实收金额与付款实付金额一致')
    else:
        ('实收金额不一致')
    order_discount=enter_workbench.get_order_discount()
    print(print('订单记录的优惠金额：',order_discount))
    if order_discount==discount[0:-1]:
        print('订单记录的优惠金额与付款优惠金额一致')
    else:
        ('优惠金额不一致')




if __name__=='__main__':
    Cash_payment()
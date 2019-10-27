from Action import login
from untils import find,Table,config_handler
from untils.config_handler import *
from untils import PageAction
from untils.PageAction import *
import random



#进入工作台
def enter_workbenchpage():
    # login.login()
    find.getElement(localtion=read_file.get_option('workbench','workbench_text'))
    print('当前位置:工作台首页')



#进入工作台-收款模块
def workbench_payment():
    enter_workbenchpage()
    PageAction.click(localtion=read_file.get_option('workbench','pay_button'))
    PageAction.pause(3)

#进入工作台-收款模块-输入手机号码
def workbench_inputPhone():
    while True:
        PageAction.input_string(localtion=read_file.get_option('workbench','number_ele'),content='15806049674')
        cardNoPhone_value=PageAction.getelement_attribute(read_file.get_option('workbench','number_ele'),attr='value')
        PageAction.pause(2)
        if len(cardNoPhone_value)==11:
            print('成功输入11位手机号码:',cardNoPhone_value)
            break
        else:
            print('手机号码位数错误,重输',cardNoPhone_value)
    PageAction.pause(1)
    PageAction.press_enter_key()
    PageAction.pause(5)
    # 定位汽油余额元素
    dieselBalance_content = PageAction.getelement_text(read_file.get_option('workbench','dieselBalance_ele'))
    if dieselBalance_content.find('汽油余额')!=-1:
        str_dieselBalance = dieselBalance_content.split("：")[1]# 汽油余额
    else:
        str_dieselBalance=0
    # 定位柴油余额元素
    gaslBalance_content = PageAction.getelement_text(read_file.get_option('workbench','gaslBalance_ele'))
    if dieselBalance_content.find('柴油余额') != -1:
        str_gaslBalance = gaslBalance_content.split("：")[1]  # 柴油余额
    else:
        str_gaslBalance=0
    # 定位通用余额元素
    commonlBalance_content = PageAction.getelement_text(read_file.get_option('workbench','commonlBalance_ele'))
    str_commonlBalance = commonlBalance_content.split("：")[1]  # 通用余额
    print('当前汽油余额:%s,柴油余额%s,通用余额:%s'%(str_dieselBalance,str_gaslBalance,str_commonlBalance))
    return [str_dieselBalance,str_gaslBalance,str_commonlBalance]

def clear_coupon():
   # 清空优惠券
    PageAction.click_SvgelementXpath(read_file.get_option('workbench','clear_coupon_button'))
    PageAction.pause(3)


def click_pay():
    # 收款操作
    PageAction.click(read_file.get_option('workbench','submit_pay'))
    PageAction.pause(3)

def input_oilPrice(price):
    #输入加油金额
    PageAction.input_string(read_file.get_option('workbench','price_ele'),content=str(price))
    PageAction.press_enter_key()
    PageAction.pause(3)

def input_oilgunNo(gunNo):
    # 定位枪号元素且输入汽油枪号
    PageAction.input_string(read_file.get_option('workbench','gunNo_ele'), content=gunNo)
    PageAction.press_enter_key()
    PageAction.pause(2)

def Balance_payment_click(): #支付方式按钮：余额支付
    return  PageAction.click(read_file.get_option('workbench','Balance_pay_button'))
    PageAction.pause(10)

def Cash_payment_click(): #支付方式按钮：现金支付
    return  PageAction.click(read_file.get_option('workbench','cash_pay_button'))
    PageAction.pause(2)

def min_payment_windows():
    #最小化收款弹窗
    PageAction.click(read_file.get_option('workbench', 'min_pay'))
    # Action.click(locatorMethod='xpath', localExpression='//button[@aria-label="Close"]/following-sibling::*[1]/div')
    PageAction.pause(3)


def close_payment_windows():
   # 关闭收款弹窗
    PageAction.click_SvgelementXpath(read_file.get_option('workbench', 'close_pay'))
   #  Action.click_SvgelementXpath(locatorMethod='xpath',
   #                                   localExpression='//span[@class="ant-modal-close-x"]/i/*[name()="svg"]/*[name()="path"]')
    PageAction.pause(3)

def get_order_realpay():
    #获取订单列表实收金额
    # 方法 1：return Action.getelement_text(locatorMethod='xpath',localExpression='//tbody[@class="ant-table-tbody"]/tr[1]/td[6]')
    # table_tagname=find.getElement_tag_name('table') #获取表格标签
    table_tagname =find.getElement(read_file.get_option('workbench','table_real_pay'))
    table_element= Table.Table(table_tagname).getCell(rowNo=2 ,colNo=6) #获取表格指定的单元格对象
    return table_element.text  #返回指定单元格对象的文本
    PageAction.pause(2)

def get_order_discount():
    #获取订单列表优惠金额
    # table_tagname=find.getElement_tag_name('table') #获取表格标签
    table_tagname = find.getElement(read_file.get_option('workbench', 'table_real_pay'))
    table_element= Table.Table(table_tagname).getCell(rowNo=2 ,colNo=7) #获取表格指定的单元格对象
    return table_element.text  #返回指定单元格对象的文本
    PageAction.pause(2)

def close_success_pay_Popup():
    PageAction.pause(2)
    #关闭支付成功确定按钮
    PageAction.click(read_file.get_option('workbench', 'close_enter'))
    # Action.pause(3)

def close_fail_pay_Popup():
    #关闭支付失败弹窗
    PageAction.pause(2)
    PageAction.click(read_file.get_option('workbench', 'cancle_button'))

def find_pop():
    PageAction.pause(2)
    find.getElement(read_file.get_option('workbench', 'tan'))

def get_receiptpaymoney():
    #获取提交订单时计算的实付金额
    receipt_value = PageAction.getelement_attribute(read_file.get_option('workbench','real_receipt'),attr='value')
    # receipt = float(receipt_value)  # 现金支付模块：实付金额浮点型
    print('订单实付金额:%s' % (receipt_value))
    PageAction.click(read_file.get_option('workbench','cash_pay_button'))
    PageAction.pause(2)
    return receipt_value

def get_receivepayment():
    # 获取提交订单时计算的应收金额
    receivepayment=PageAction.getelement_text(read_file.get_option('workbench','receiver_pay'))
    return receivepayment[0:-1]
    PageAction.pause(3)

def get_discount():
    #获取提交订单时计算的优惠金额
    discount_value=PageAction.getelement_text(read_file.get_option('workbench','discount_ele'))
    discount=discount_value[0:-1]
    return  discount
    PageAction.pause(2)

#获取汽油枪号
def get_diesegunNo():
    gunNo=config_handler.Parse_JYH_Config().get_option('gunNo_info','diese_gunNo')
    return gunNo
    PageAction.pause(1)

#获取柴油枪号
def get_gasgunNo():
    gunNo=config_handler.Parse_JYH_Config().get_option('gunNo_info','gas_gunNo')
    return gunNo



def input_cash_receipt(receipt):
    Manual_input_cash=PageAction.input_string(read_file.get_option('workbench','Manual_input_cash'),content=receipt)

def get_cash_receipt():
    Manual_input_cash=PageAction.getelement_attribute(read_file.get_option('workbench','Manual_input_cash'),attr='value')
    if Manual_input_cash:
        return float(Manual_input_cash)
if __name__ =="__main__":
    # workbench_payment()
    # print(workbench_payment())
    a,b,c =workbench_payment()
    print(a,b,c)
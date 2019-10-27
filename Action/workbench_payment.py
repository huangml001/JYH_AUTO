from Action import login,enter_workbench
from untils import find,config_handler
from untils import PageAction
import random

#进入工作台-收款-检查汽油余额
def workbench_payment():
    enter_workbench.enter_workbenchpage()
    PageAction.click(locatorMethod='xpath',localExpression='//div[.="收款"]')
    while True:
        PageAction.input_string(locatorMethod='id',localExpression='cardNoPhone',content='15806049674')
        # cardNoPhone_elem=find.getElement(localType='id', localExpression='cardNoPhone')
        cardNoPhone_value=PageAction.getelement_attribute(locatorMethod='id', localExpression='cardNoPhone',attr='value')
        if len(cardNoPhone_value)==11:
            print('成功输入11位手机号码:',cardNoPhone_value)
            break
        else:
            print('手机号码位数错误,重输',cardNoPhone_value)
    PageAction.pause(1)
    PageAction.press_enter_key()
    PageAction.pause(2)
    #定位枪号元素且输入汽油枪号10
    PageAction.input_string(locatorMethod='id',localExpression="gunNo",content=config_handler.Parse_JYH_Config().get_option('gunNo_info','diese_gunNo'))
    PageAction.press_enter_key()
    PageAction.pause(5)
    #优惠券内容
    # coupon =find.getElement(localType='xpath',localExpression='//label[@title="优惠券"]/parent ::*/following-sibling::*/div/span/div').text
    #清空优惠券
    PageAction.click_SvgelementXpath(locatorMethod='xpath',localExpression="//span[@class='ant-form-item-children']/i/*[name()='svg']/*[name()='path'][2]")
    PageAction.pause(2)


if __name__ == "__main__":
    workbench_payment()

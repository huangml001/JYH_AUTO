# -*-coding:utf-8 -*-
from selenium import webdriver
import unittest,time
#当前文件所在目录下导入Table.py文件中的Table类
from untils.Table import Table
class TestTableOpertion(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def testTable(self):
        url='D:\\book\\html.html'
        self.driver.get(url)
        #获取被测试页面中的表格元素，并存储在webTable变量中
        webTable=self.driver.find_elements_by_tag_name('table')
        table=Table(webTable)
        #统计行数
        print(table.getRowCount())
        #统计表格列数
        print(table.getColumnCount())
        #获取表格中第2行第3列单元格对象
        cell=table.getCell(2,3)
        print(cell)
        #断言获取的单元格文本内容是否是第2行，第3列
        self.assertAlmostEqual('第二行第三列',cell.text)
        #获取表格中第3行第2列单元格中的输入对象
        cellInput=table.getWebElementInCell(3,2,'tag name','input')
        #找到的输入框中输入'第3行第2列表格被找到’关键字内容
        cellInput.send_keys('第三行第二列表格被找到')
        #等待3秒，肉眼查看输入效果
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()

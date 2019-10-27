# -*-coding:utf-8 -*-
class Table(object):
    #定义一个私有属性_table，用于存放table对象
    __table=''
    def __init__(self,table):
        #Table类的构造方法
        self.setTable(table)

    def setTable(self,table):
        #对私有属性__table进行赋值操作  table:表格
        self.__table=table

    def getTable(self):
        return self.__table

    def getRowCount(self):
        #返回table对象中所有的tr标签元素对象行数 tr:行
        return len(self.__table.find_elements_by_tag_name('tr'))
    
    def getColumnCount(self):
        #返回table对象中的列数
        return len(self.__table.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td'))
    
    def getCell(self,rowNo,colNo):
        #返回表格中某行某列的单元格对象
        try:
            #找到表格中的某一行因为行号从0开始，例如要找第3行，则需要3-1=2来获取第3行tr元素对象
            currentRow=self.__table.find_elements_by_tag_name('tr')[rowNo-1]
           #在找到某行基础上，再找到这行中的某一列，列号也从0开始
            # print(len(currentRow.find_elements_by_tag_name('td')))
            currentCol=currentRow.find_elements_by_tag_name('td')[colNo-1]
            #返回找到的单元格对象
            return currentCol
        except Exception as e:
            raise e
        
    def getWebElementInCell(self,rowNo,colNo,by,value):
        #获取表格中某行某列的单元格中某个页面元素对象,by表示定位页面元素的方法，
        # 比如id，value表示定位表达式比如:query
        try:
            currentRow=self.__table.find_elements_by_tag_name('tr')[rowNo-1]
            currentCol=currentRow.find_elements_by_tag_name('td')[colNo-1]
            #获取具体某个单元格中某个页面元素
            element=currentCol.find_element(by=by,value=value)
            #返回找到的页面元素对象
            return element
        except Exception as e:
            raise e
        

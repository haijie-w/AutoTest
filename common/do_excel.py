# coning = utf-8
__author__ = 'Aimee'

import xlrd
from xlutils.copy import copy
import json

class OperationExcel:
    def __init__(self,file_name =None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../test_data/TestCase_OOLA_APP.xls'
            self.sheet_id = 1
        self.data = self.get_data()

    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #read excel数据 成dict
    def read_excel_to_dict(self):
        nrows = self.data.nrows
        data_dict =[self.data.row_values(i) for i in range(0, nrows)]
        result =[dict(zip(data_dict[0], data_dict[i])) for i in range(1, len(data_dict))]
        return result

    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name,formatting_info = True)
        write_data = copy(read_data) #复制一份数据
        sheet_data = write_data.get_sheet(1) #拿到sheet数据
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)
        return write_data

    #写入响应数据
    def write_Response(self,row,value):
        self.write_value(row,12,value)
    #写入结果

    def write_Result(self,row,value):
        self.write_value(row,13,value)

if __name__ == '__main__':
    x = OperationExcel()
    y = x.read_excel_to_dict()
    z = y[0]['params']
    print(type(z))
    print(json.dumps(z))








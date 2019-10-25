"""
author:xiaoma
datetime:2019/10/21 9:23
describe:该模块用于操作读取excel,获取某一行、某一格、某一列的内容
"""
import xlrd
from xlutils.copy import copy


class ExcelReadUtil:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../test_case/interface.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        """
        读取excel文件
        :return:
        """
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """
        获取有值单元格的行数
        :return:
        """
        tables = self.data
        return tables.nrows

    def get_cell_value(self, row, col):
        """
        获取单元格的内容
        :param row:
        :param col:
        :return:
        """
        return self.data.cell_value(row, col)

    def write_value(self,row,col,value):
        """
        测试执行的结果写入对应的行中
        :param row:
        :param col:
        :param value:
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    def get_rows_data(self,case_id):
        """
        根据case_id查找到对应行的内容
        :param case_id:
        :return:
        """
        row_num = self.get_rows_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    def get_rows_num(self,case_id):
        """
        根据对应的case_id找到对应的行号
        :param case_id:
        :return:
        """
        num = 0
        cols_data = self.get_cols_data()
        for i in cols_data:
            if case_id in i:
                return num
            num += 1


    def get_row_values(self,row):
        """
        根据行号来查找行的内容
        :param row:
        :return:
        """
        tables = self.data
        row_value = tables.row_values(row)
        return row_value

    def get_cols_data(self, col_id=None):
        """
        获取某一列的内容
        :param col_id:
        :return:
        """
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols



if __name__ == '__main__':
    opers = ExcelReadUtil()
    #print (opers.get_data().nrows)
   # print(opers.get_call_value(1,1))
    #print(opers.get_cols_data(0))
    #print(opers.get_row_values(1))
    print(opers.get_rows_num('kid17-001'))
    #print(opers.get_lines())
    #print(opers.get_rows_data("kid17-001"))

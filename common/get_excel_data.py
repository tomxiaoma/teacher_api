"""
author:xiaoma
datetime:2019/10/22 14:20
describe:该模块用于操作excel中对应每一列的数据
"""
from excel_read_util import ExcelReadUtil
import constant_excel
from json_read_util import JSONReadUtil


class GetData:

    def __init__(self):
        self.read_excel = ExcelReadUtil()

    def get_case_lines(self):
        """
        获取excel的行数（case的个数），只获取有值的
        :return:
        """
        return self.read_excel.get_lines()

    def get_is_run(self,row):
        """
        是否执行,excel中对于【是否运行该测试用例列】
        :param row:
        :return:
        """
        flag = None
        col = int(constant_excel.get_is_run())
        run_model = self.read_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self,row):
        """
        是否包含header请求头信息，excel中对应【鉴权cookie】
        :param row:
        :return:
        """
        col = int(constant_excel.get_header())
        header = self.read_excel.get_cell_value(row,col)
        if header == 'yes':
            return constant_excel.get_header_value()
        else:
            return None

    def get_request_method(self, row):
        """
        获取请求方式，excel中对应【接口请求方式】
        :param self:
        :param row:
        :return:
        """
        col = int(constant_excel.get_run_way())
        request_method = self.read_excel.get_cell_value(row, col)
        return request_method

    def get_request_url(self, row):
        """
        获取url，excel中对应【接口请求url】
        :param row:
        :return:
        """
        col = int(constant_excel.get_request_url())
        url = self.read_excel.get_cell_value(row, col)
        return url

    def get_model_name(self, row):
        """
        获取模块名称，excel中对应【测试用例描述】
        :param row:
        :return:
        """
        col = int(constant_excel.get_model_name())
        model_name = self.read_excel.get_cell_value(row, col)
        return model_name

    def get_request_data(self, row):
        """
        获取请求数据
        :param row:
        :return:
        """
        col = int(constant_excel.get_data())
        data = self.read_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    def get_data_for_json(self, row):
        """
        通过关键字获取请求数据（json）
        :param row:
        :return:
        """
        read_json = JSONReadUtil()
        request_data = read_json.get_key_data(self.get_request_data(row))
        return request_data

    def get_expcet_data(self, row):
        """
        获取预期结果，对应excel中【测试预期结果列】
        :param row:
        :return:
        """
        col = int(constant_excel.get_expect())
        expect = self.read_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    def weite_result(self,row,value):
        """
        在excel中写入测试结果，对应excel中【测试实际结果列】
        :param row:
        :param value:
        :return:
        """
        col =int(constant_excel.get_result())
        self.read_excel.write_value(row,col,value)

    def get_depend_key(self,row):
        """
        获取依赖数据的key
        :param row:
        :return:
        """
        col = int(constant_excel.get_data_depend())
        denpend_key = self.read_excel.get_cell_value(row,col)
        if denpend_key =="":
            return None
        else:
            return denpend_key

    def is_denpend(self,row):
        """
        判断是否有用例依赖
        :param row:
        :return:
        """
        col = int(constant_excel.get_field_depend())
        denpend_case_id = self.read_excel.get_cell_value(row, col)
        if denpend_case_id == "":
            return None
        else:
            return denpend_case_id

    def get_field_depend(self,row):
        """
        获取依赖字段
        :param row:
        :return:
        """
        col = int(constant_excel.get_field_depend())
        denpend_field = self.read_excel.get_cell_value(row,col)
        if denpend_field == "":
            return None
        else:
            return denpend_field

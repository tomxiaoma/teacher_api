"""
author:xiaoma
datetime:2019/10/23 11:28
describe:主要是针对依赖数据，比如一些接口的执行，依赖上一个接口返回的数据
"""
from util.excel_read_util import ExcelReadUtil
from base.request_method import RunMethod
from common.get_excel_data import GetData
from jsonpath_rw import jsonpath,parse
import json


class DependData:
    def __init__(self,case_id):
        self.read_excel = ExcelReadUtil()
        self.case_id = case_id
        self.data = GetData()

    def get_case_line_data(self,case_id):
        """
        根据case_id获取整行数据
        :param case_id:
        :return:
        """
        return self.read_excel.get_rows_data(self.case_id)

    def run_dependent(self):
        """
        执行依赖测试，并返回结果
        :return:
        """
        run_method = RunMethod()
        row_num = self.read_excel.get_rows_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method,url,request_data,header)
        return json.loads(res)

    def get_data_for_key(self,row):
        """
        根据依赖的key获取执行依赖接口的响应结果，并且返回
        :param row:
        :return:
        """
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


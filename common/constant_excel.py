"""
# author:xiaoma
# datetime:2019/10/21 9:50
describe:该模块主要是针对excel中对应的每一列，作为一个常量池
"""


class ConstantExcel:
    case_Id = '0'
    model_name = '1'
    request_url = '2'
    is_run = '3'
    request_type = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    request_data = '9'
    expect = '10'
    result = '11'


def get_id():
    return ConstantExcel.case_Id


def get_model_name():
    return ConstantExcel.model_name


def get_request_url():
    return ConstantExcel.request_url


def get_is_run():
    return ConstantExcel.is_run


def get_run_way():
    return ConstantExcel.request_type


def get_header():
    return ConstantExcel.header


def get_case_depend():
    return ConstantExcel.case_depend


def get_data_depend():
    return ConstantExcel.data_depend


def get_field_depend():
    return ConstantExcel.field_depend


def get_data():
    return ConstantExcel.request_data


def get_expect():
    return ConstantExcel.expect


def get_result():
    return ConstantExcel.result


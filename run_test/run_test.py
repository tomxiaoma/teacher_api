"""
author:xiaoma
datetime:2019/10/22 13:32
"""
from base.request_method import RunMethod
from common.get_excel_data import GetData
from util.contain_util import ContainUtil
from common.get_depende_data import DependData
from util.send_email_util import SendEmailUtil
from config.loggingReader import *


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = GetData()
        self.contain_util = ContainUtil()
        self.send_email = SendEmailUtil()

    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.get_data.get_case_lines()
        #获取所有有值的行
        for i in range(1,rows_count):
            is_run = self.get_data.get_is_run(i)
            #判断该条用例是否是执行的，对照excel中的【是否执行用例】字段
            if is_run:
                url = self.get_data.get_request_url(i)
                model_name = self.get_data.get_model_name(i)
                method = self.get_data.get_request_method(i)
                request_data = self.get_data.get_data_for_json(i)
                expect = self.get_data.get_expcet_data(i)
                header = self.get_data.is_header(i)
                depend_case = self.get_data.is_denpend(i)
                #判断执行测试用例时，是否有依赖的测试用例，如果excel中依赖为空时直接跳过
                if depend_case != None:
                    self.depend_data = DependData()
                    #获取响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.get_data.get_field_depend(i)
                    request_data[depend_key] = depend_response_data
                res = self.run_method.run_main(method, url, request_data, header)

                if self.contain_util.is_contain(expect,res):
                    self.get_data.weite_result(i, "测试通过")
                    pass_count.append(i)
                    logging.info("测试通过")
                else:
                    self.get_data.weite_result(i, res)
                    fail_count.append(i)
                    logging.info("测试失败。测试用例描述:%s ,失败路由：%s" %(model_name,url))
                #print(res)
        logging.info("邮件已发送，请注意查收")
        self.send_email.send_test_report(pass_count,fail_count)



if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

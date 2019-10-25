"""
author:xiaoma
datetime:2019/10/21 11:20
describe:对json文件进行读取，并且根据对于的获取key的方法来拿到请求数据
"""
import json


class JSONReadUtil:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = "../API/request.json"
        else:
            self.file_path = file_path
        self.data = self.read_json_data()

    def read_json_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    def get_key_data(self,key):
        """
        根据key获取数据
        :param key:
        :return:
        """
        return self.data[key]


if __name__ == "__main__":
    oper = JSONReadUtil()
    print(oper.get_key_data("appKey"))


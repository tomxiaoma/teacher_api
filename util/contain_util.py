# author:xiaoma
# datetime:2019/10/22 16:31


class ContainUtil:

    def is_contain(self,first_value,second_value):
        """
        判断一个字符串是否在一个字符串中
        :param str_one:
        :param str_two:
        :return:
        """
        if first_value is None:
            return "预期结果为空"
        if first_value in second_value:
            return True
        else:
            return False


"""
author:xiaoma
datetime:2019/10/23 17:46
describe:用于发送邮件，在测试结束之后发送邮件给对应的用户
"""
import smtplib
from email.mime.text import MIMEText
from config.yamlReader import *


class SendEmailUtil:
    global send_user
    global email_host
    global password
    email_host = data['email_host']
    send_user = data['send_user']
    password = data['password']

    def send_mail(self, user_list, sub, content):
        user = data['send_name'] + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_test_report(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        receive_user_list = data['receive_user_list']
        title = data['title']
        content = "一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (
        count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(receive_user_list, title, content)


if __name__ == '__main__':
    sen = SendEmailUtil()
    #user_list=['545736616@qq.com']
    #sub = "接口自动化测试报告"
    #content = "真是服了"
    #sen.send_mail(user_list,sub,content)
    sen.send_test_report([1, 2, 3, 4], [2, 3, 4, 5, 6, 7])
import HtmlTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import os
import time


def send_mail(file_new):

    # 读取邮件正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 邮件对象，三个参数：第一个为文本内容，第二个 html 设置文本格式，第三个 utf-8 设置编码
    msg = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件主题
    msg['Subject'] = Header('nbp automated test report', 'utf-8')
    # 邮件发送者
    msg['From'] = Header('FromSomeone', 'utf-8')
    # 邮件接收者
    msg['To'] = Header('ToSomeone', 'utf-8')

    # smtp对象，从smtp服务器发送
    smtp = smtplib.SMTP('smtp.163.com')
    smtp.login('account', 'password')
    smtp.sendmail('sender', 'receivers', msg.as_string())
    smtp.quit()
    print('email has send out.')


# 查找unittest生成的报告
def new_report(test_report):
    # 列出test_report目录下所有文件
    lists = os.listdir(test_report)
    # 根据时间排序
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    # 格式化时间，%Y年 %m月 %d日 %H时 %M分 %S秒
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 根据unittest的报告生成测试报告
    file_name = './nbp/report/' + now + 'result.htm'
    with open(file_name, 'w') as fp:
        # HTMLTestRunner是TestRunner的子类，可以调用run运行测试用例
        runner = HtmlTestRunner.HTMLTestRunner(stream=fp, report_title='nbp automated test report')
        # 第一个参数：测试用例的目录；第二个参数：测试用例模式匹配，一个*_sta.py就是一个测试用例，每个测试用例打开一次浏览器
        # 生成一个测试用例组：test_suite，包含多个测试用例
        test_suite = unittest.defaultTestLoader.discover(r'.\nbp\test_case', pattern='*_sta.py')
        # 运行测试用例组
        runner.run(test_suite)

# coning = utf-8
__author__ = 'Aimee'

import os,sys
path= os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(path)
import unittest
from  config.project_path import data_path,report_path,log_path
from test_case.test_oola import *
from common.send_mail import sendEmail
from common.HTMLTestRunnerNew import HTMLTestRunner


#指定执行某个测试用例
s = unittest.TestSuite()
s.addTests(unittest.TestLoader().loadTestsFromTestCase(Oola_testCase))
# now = time.strftime('%Y-%m-%d')
# report_name = 'TestReport' + now + '.html'
# file_path = report_path + '\\' + report_name


#执行所有测试
''''-case_dir:这个是待执行用例的目录。

-pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。

-top_level_dir：这个是顶层目录的名称，一般默认等于None就行了'''

# discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)

filename = open(report_path, 'wb')
runner = HTMLTestRunner(
    stream=filename,
    title='OOLA接口自动化测试报告',
    description='OOLA接口自动化测试报告',
    tester='AIMEE')
runner.run(s)
# runner.run(discover)

#将所有文件作为附加发送的文件处理成列表

filepath=[report_path,data_path,log_path]
sendEmail().send_main(pass_count,fail_count)










